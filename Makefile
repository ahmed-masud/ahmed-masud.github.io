PY  = python3
SRC = resume-src/build.py

.PHONY: help new tailor render render-all list status export

help:
	@echo "Resume builder commands:"
	@echo ""
	@echo "  make new    COMPANY=Acme ROLE='Engineering Manager' [DATE=2026-06-16] [SOURCE=LinkedIn] [URL=https://...]"
	@echo "  make tailor COMPANY=Acme ROLE='Engineering Manager' JD=path/to/jd.txt [MODEL=mistral] [DATE=...] [RENDER=1]"
	@echo "              [HOST=http://remote:11434] [APIKEY=secret]"
	@echo "  # or set env vars: OLLAMA_HOST=http://remote:11434 OLLAMA_API_KEY=secret"
	@echo "  make render JOB=ACME_2026-06-16"
	@echo "  make render-all"
	@echo "  make list"
	@echo "  make status JOB=ACME_2026-06-16 STATUS=interview"
	@echo "  make export"
	@echo ""
	@echo "LLM tailoring requires Ollama (https://ollama.ai) running locally."
	@echo "Recommended models: ollama pull mistral   (4.4 GB, best results)"
	@echo "                    ollama pull llama3.2  (2 GB, good results)"
	@echo "Available models:   ollama list"
	@echo ""

new:
	@$(PY) $(SRC) new \
	  --company "$(COMPANY)" \
	  --role    "$(ROLE)" \
	  $(if $(DATE),    --date   "$(DATE)") \
	  $(if $(SOURCE),  --source "$(SOURCE)") \
	  $(if $(URL),     --url    "$(URL)")

tailor:
	@$(PY) $(SRC) tailor \
	  --company "$(COMPANY)" \
	  --role    "$(ROLE)" \
	  --jd      "$(JD)" \
	  $(if $(MODEL),  --model   "$(MODEL)") \
	  $(if $(DATE),   --date    "$(DATE)") \
	  $(if $(HOST),   --host    "$(HOST)") \
	  $(if $(APIKEY), --api-key "$(APIKEY)") \
	  $(if $(RENDER), --render)

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
