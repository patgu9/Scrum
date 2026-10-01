#!/usr/bin/env python3
"""Validate the Product Design Markdown contract; no third-party dependencies.

This checks structure and references, not evidence, consent, or semantic quality.
"""

import argparse
from collections import Counter
from datetime import date
from pathlib import Path
import re
import sys


def visible(text):
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    result, fence = [], None
    for line in text.splitlines():
        match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if match:
            token = match.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            result.append(line)
    return "\n".join(result)


def sections(text):
    matches = list(re.finditer(r"^(#{1,6}) (.+)$", text, re.M))
    return [(m.group(1) + " " + m.group(2),
             text[m.end():matches[i + 1].start() if i + 1 < len(matches) else len(text)])
            for i, m in enumerate(matches)]


def cells(line):
    return tuple(x.strip() for x in re.split(r"(?<!\\)\|", line.strip()[1:-1]))


def tables(text):
    lines = text.splitlines()
    result = []
    for i in range(len(lines) - 1):
        if not (lines[i].strip().startswith("|") and lines[i].strip().endswith("|")):
            continue
        sep = lines[i + 1].strip()
        if not (sep.startswith("|") and sep.endswith("|")):
            continue
        if not all(re.fullmatch(r":?-{3,}:?", x) for x in cells(sep)):
            continue
        rows = []
        for line in lines[i + 2:]:
            if not (line.strip().startswith("|") and line.strip().endswith("|")):
                break
            rows.append(cells(line))
        result.append((cells(lines[i]), rows))
    return result


def shape(heading):
    if heading.startswith("## Design Doc : "):
        return "## Design Doc : <title>"
    if re.fullmatch(r"#### Feature [1-9]\d* — .+", heading):
        return "#### Feature <n> — <name>"
    return heading


def validate(document, template):
    errors = []
    actual, contract = visible(document), visible(template)
    nodes, expected = sections(actual), sections(contract)
    feature_at = next(i for i, (h, _) in enumerate(expected) if h.startswith("#### Feature "))
    prefix = [shape(h) for h, _ in expected[:feature_at]]
    block = [shape(h) for h, _ in expected[feature_at:]]
    headings = [shape(h) for h, _ in nodes]
    count, rem = divmod(max(0, len(headings) - len(prefix)), len(block))
    if count < 1 or rem or headings != prefix + block * count:
        errors.append("Heading order differs from template; preserve all sections and repeat only the Feature block.")
        return errors
    if not re.match(r"\A\s*## Design Doc : \S", actual):
        errors.append("The document must start with its Design Doc title, without a preface.")

    metadata = re.findall(r"^- ([A-Za-z]+): (.+)$", nodes[0][1], re.M)
    if [k for k, _ in metadata] != ["Status", "Mode", "Date", "Stage"]:
        errors.append("Metadata must be Status, Mode, Date, Stage, once each in that order.")
    meta = dict(metadata)
    if meta.get("Status") not in {"DRAFT", "IN_REVIEW", "APPROVED"}:
        errors.append("Invalid Status.")
    if meta.get("Mode") not in {"Startup", "Builder"}:
        errors.append("Invalid Mode.")
    if meta.get("Stage") != "Think":
        errors.append("Stage must be Think.")
    try:
        value = meta.get("Date", "")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
            raise ValueError
        date.fromisoformat(value)
    except ValueError:
        errors.append("Date must be a valid YYYY-MM-DD date.")

    # Detect only literal placeholders from the actual template, not dollar prices.
    for placeholder in set(re.findall(r"\$[^$\n]+\$", contract)):
        if placeholder in actual:
            errors.append("Unfilled template placeholder: " + placeholder)
    if "<!--" in document:
        errors.append("Remove instructional HTML comments from the final document.")

    section_rows = {}
    for i, (heading, body) in enumerate(nodes):
        template_i = i if i < feature_at else feature_at + (i - feature_at) % len(block)
        expected_body = expected[template_i][1]
        for label in re.findall(r"^(?:- )?\*\*([^*]+):\*\*", expected_body, re.M):
            if "(optional)" in label or re.fullmatch(r"F\d+-AC\d+", label):
                continue
            if "**" + label + ":**" not in body:
                errors.append(f"{heading}: missing label {label}.")
        found_tables = tables(body)
        for table_header, _ in tables(expected_body):
            matches = [rows for header, rows in found_tables if header == table_header]
            if heading == "##### Key Examples" and not matches:
                continue  # Narrative examples are checked below.
            if len(matches) != 1:
                errors.append(f"{heading}: expected exactly one table with headers {table_header}.")
                continue
            rows = matches[0]
            section_rows[i] = rows
            if not rows or any(len(row) != len(table_header) or not all(row) for row in rows):
                errors.append(f"{heading}: table requires nonempty, complete rows.")
        if not body.strip() and not heading.startswith(("#### Feature ", "### Background", "### Solution Design", "### Requirements")):
            errors.append(f"{heading}: empty section.")

    sc_i = next(i for i, (h, _) in enumerate(nodes) if h == "#### Success Criteria")
    sc_ids = [row[0] for row in section_rows.get(sc_i, []) if row]
    if any(not re.fullmatch(r"SC[1-9]\d*", x) for x in sc_ids):
        errors.append("Success Criteria rows must start with SC IDs.")
    identities = list(sc_ids)
    for i in range(feature_at, len(nodes), len(block)):
        feature = "F" + re.match(r"#### Feature (\d+)", nodes[i][0]).group(1)
        identities.append(feature)
        story, rule_body, example_body = nodes[i + 1][1], nodes[i + 2][1], nodes[i + 3][1]
        story_parts = [re.search(r"^>\s*" + part + r"\s+\S", story, re.M | re.I)
                       for part in ("In order to", "as a", "I want to")]
        if not all(story_parts) or [m.start() for m in story_parts if m] != sorted(m.start() for m in story_parts if m):
            errors.append(f"{feature}: user story must contain In order to, as a, I want to in order.")
        linked = re.search(r"\*\*Related Success Criteria:\*\*([^\n]+)", story)
        linked_ids = re.findall(r"\bSC\d+\b", linked.group(1)) if linked else []
        if not linked_ids or not set(linked_ids) <= set(sc_ids):
            errors.append(f"{feature}: Related Success Criteria must reference existing SC IDs.")
        rules = re.findall(r"^- \*\*(F\d+-AC[1-9]\d*):\*\*\s+\S[^\n]*", rule_body, re.M)
        identities.extend(rules)
        if not rules or any(not x.startswith(feature + "-") for x in rules):
            errors.append(f"{feature}: requires business rules with this Feature's AC IDs.")
        examples = []
        example_rows = section_rows.get(i + 3)
        if example_rows is not None:
            for row in example_rows:
                if len(row) != 5:
                    continue
                eid = re.match(r"(F\d+-E[1-9]\d*)\b", row[0])
                examples.append((eid.group(1) if eid else "", row[1]))
        else:
            starts = list(re.finditer(r"^\*\*(F\d+-E[1-9]\d*):[^\n]+\*\*\s*$", example_body, re.M))
            for j, match in enumerate(starts):
                chunk = example_body[match.end():starts[j + 1].start() if j + 1 < len(starts) else len(example_body)]
                fields = {k: v.strip() for k, v in re.findall(r"^- \*\*(Related Rule|Given|When|Then):\*\*([^\n]*)", chunk, re.M)}
                if set(fields) != {"Related Rule", "Given", "When", "Then"} or not all(fields.values()):
                    errors.append(f"{match.group(1)}: requires Related Rule, Given, When, Then.")
                examples.append((match.group(1), fields.get("Related Rule", "")))
        covered = set()
        if not examples:
            errors.append(f"{feature}: requires key examples, as a table or narrative.")
        for eid, references in examples:
            identities.append(eid)
            linked_rules = set(re.findall(r"\bF\d+-AC\d+\b", references))
            if not eid.startswith(feature + "-E") or not linked_rules or not linked_rules <= set(rules):
                errors.append(f"{eid or feature}: invalid example ID or rule reference.")
            covered.update(linked_rules)
        if set(rules) - covered:
            errors.append(f"{feature}: rules without examples: {sorted(set(rules) - covered)}.")

    duplicates = [x for x, n in Counter(identities).items() if n > 1]
    if duplicates:
        errors.append(f"Duplicate definitions: {duplicates}.")
    rec_i = next(i for i, (h, _) in enumerate(nodes) if h == "#### Recommended Approach")
    for row in section_rows.get(rec_i, []):
        if len(row) != 4:
            continue
        flags = re.findall(r"Blocks approval:\s*(Yes|No)\b", row[1])
        if len(flags) != 1:
            errors.append("Every premise/question row needs one Blocks approval: Yes or No in Statement and Impact.")
        elif flags[0] == "Yes" and meta.get("Status") in {"IN_REVIEW", "APPROVED"}:
            errors.append("Approval-blocking questions require DRAFT status.")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("document", type=Path)
    parser.add_argument("--template", type=Path,
                        default=Path(__file__).resolve().parents[1] / "assets/design-doc-template.md")
    args = parser.parse_args()
    try:
        issues = validate(args.document.read_text(), args.template.read_text())
    except (OSError, UnicodeError, StopIteration, IndexError) as exc:
        print(f"Cannot validate: {exc}", file=sys.stderr)
        return 2
    if issues:
        print("STRUCTURE FAIL")
        for issue in issues:
            print("- " + issue)
        return 1
    print("STRUCTURE PASS — semantic quality, evidence, and user approval still require review.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
