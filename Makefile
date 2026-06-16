PY  = python3
SRC = resume-src/build.py

.PHONY: help new render render-all list status export

help:
	@echo "Resume builder commands:"
	@echo ""
	@echo "  make new COMPANY=Acme ROLE='Engineering Manager' [DATE=2026-06-16] [SOURCE=LinkedIn] [URL=https://...]"
	@echo "  make render JOB=ACME_2026-06-16"
	@echo "  make render-all"
	@echo "  make list"
	@echo "  make status JOB=ACME_2026-06-16 STATUS=interview"
	@echo "  make export"
	@echo ""

new:
	@$(PY) $(SRC) new \
	  --company "$(COMPANY)" \
	  --role    "$(ROLE)" \
	  $(if $(DATE),    --date   "$(DATE)") \
	  $(if $(SOURCE),  --source "$(SOURCE)") \
	  $(if $(URL),     --url    "$(URL)")

render:
	@$(PY) $(SRC) render $(JOB)

render-all:
	@$(PY) $(SRC) render-all

list:
	@$(PY) $(SRC) list

status:
	@$(PY) $(SRC) status $(JOB) $(STATUS)

export:
	@$(PY) $(SRC) export
