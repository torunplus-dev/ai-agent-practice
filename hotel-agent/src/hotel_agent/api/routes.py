from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from hotel_agent.api.schemas import SearchRequest, SearchResponse
from hotel_agent.loop.planner import plan_and_search

router = APIRouter()

EDITOR_HTML = """<!doctype html>
<html lang=\"ja\">
  <head>
    <meta charset=\"utf-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
    <title>Editor Pane</title>
    <style>
      :root {
        color-scheme: light;
        font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      }

      body {
        margin: 0;
        min-height: 100vh;
        display: grid;
        place-items: center;
        background: #f3f4f6;
      }

      .app-shell {
        width: min(960px, 92vw);
        min-height: 65vh;
        border: 1px solid #d1d5db;
        border-radius: 12px;
        background: #ffffff;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
        display: grid;
        grid-template-columns: 1fr minmax(520px, 2fr) 1fr;
      }

      .pane {
        padding: 16px;
      }

      .center-pane {
        border-inline: 1px solid #e5e7eb;
      }

      h1 {
        margin: 0 0 12px;
        font-size: 1.1rem;
      }

      table {
        width: 100%;
        border-collapse: collapse;
        font-size: 0.92rem;
      }

      th,
      td {
        border: 1px solid #e5e7eb;
        padding: 10px;
        text-align: left;
      }

      thead {
        background: #f9fafb;
      }
    </style>
  </head>
  <body>
    <main class=\"app-shell\">
      <aside class=\"pane\">ナビゲーション</aside>
      <section class=\"pane center-pane\" aria-label=\"編集用ペイン\">
        <h1>ログ / レコード / 設定一覧</h1>
        <table aria-label=\"ログ・レコード・設定一覧テーブル\">
          <thead>
            <tr>
              <th scope=\"col\">種別</th>
              <th scope=\"col\">名前</th>
              <th scope=\"col\">最終更新</th>
              <th scope=\"col\">状態</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>ログ</td>
              <td>検索実行ログ</td>
              <td>2026-02-19 09:30</td>
              <td>保存済み</td>
            </tr>
            <tr>
              <td>レコード</td>
              <td>ホテル候補一覧</td>
              <td>2026-02-19 09:28</td>
              <td>レビュー待ち</td>
            </tr>
            <tr>
              <td>設定</td>
              <td>通知ルール</td>
              <td>2026-02-18 17:45</td>
              <td>有効</td>
            </tr>
          </tbody>
        </table>
      </section>
      <aside class=\"pane\">インスペクター</aside>
    </main>
  </body>
</html>
"""


@router.get("/", response_class=HTMLResponse)
def editor() -> HTMLResponse:
    return HTMLResponse(content=EDITOR_HTML)


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/search", response_model=SearchResponse)
def search(request: SearchRequest) -> SearchResponse:
    return plan_and_search(request)
