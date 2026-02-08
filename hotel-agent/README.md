# Hotel Search Agent (MVP)

自然言語の prompt を入力として、固定JSONスキーマでホテル検索結果を返す最小APIです。
Tripadvisor コネクタはスタブで、外部呼び出しは行いません。

## クイックスタート（uv）
```bash
cd hotel-agent
uv sync
uv run uvicorn hotel_agent.main:app --reload
```

## 動作確認
```bash
curl -s http://127.0.0.1:8000/health
```

```bash
curl -s -X POST http://127.0.0.1:8000/search \
  -H 'Content-Type: application/json' \
  -d '{"prompt":"東京で3泊、駅近のホテル"}'
```

## 構成
- `src/hotel_agent/api/`: FastAPI ルートとスキーマ
- `src/hotel_agent/loop/`: ルーター/プランナー（将来拡張）
- `src/hotel_agent/connectors/`: 検索コネクタ抽象と実装
- `config/`: 設定ファイルの配置

## 設定
- `config/config.yaml` があれば読み込みます（無ければ例を参照）。
- 秘密情報は `.env` で管理します（`/hotel-agent/.env.example`）。
