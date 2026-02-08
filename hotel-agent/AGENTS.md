# Hotel Agent Repo Rules

## Purpose
Beginner-safe hotel search agent MVP with fixed JSON responses.

## Must Read
- `docs/AGENT_SPEC.md`
- `src/hotel_agent/api/schemas.py`
- `src/hotel_agent/loop/`
- `src/hotel_agent/connectors/`

## Rules
- APIレスポンスは固定JSON。自由文は `explanation` のみ。
- 外部promptをそのまま信頼しない（将来の注入対策を意識）。
- 変更時は `api/schemas.py` と `loop/` と `connectors/` の責務を守る。
