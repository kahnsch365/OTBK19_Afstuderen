#!/usr/bin/env bash
# Installs dependencies in cloud sessions (desktop/iOS app) so tests can run.
# Local sessions are skipped. Extend per project if needed; keep it quiet:
# anything printed to stdout lands in Claude's context.
[ "$CLAUDE_CODE_REMOTE" = "true" ] || exit 0
cd "$CLAUDE_PROJECT_DIR" || exit 0

{
  if [ -f package-lock.json ]; then npm ci
  elif [ -f pnpm-lock.yaml ]; then pnpm install --frozen-lockfile
  elif [ -f yarn.lock ]; then yarn install --frozen-lockfile
  elif [ -f package.json ]; then npm install
  fi
  if [ -f requirements.txt ]; then pip install -r requirements.txt
  elif [ -f pyproject.toml ]; then pip install -e .
  fi
} >/dev/null 2>&1 || echo "session-start: dependency install failed, run it manually."

exit 0
