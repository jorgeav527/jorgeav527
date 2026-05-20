.PHONY: help install-node-modules install-zola setup dev build clean

help:
	@echo "Available commands:"
	@echo "  make install-node-modules - Install Node dependencies"
	@echo "  make install-zola         - Install Zola locally"
	@echo "  make setup                - Install both Node deps and Zola"
	@echo "  make dev                  - Run development server"
	@echo "  make build                - Build production site"
	@echo "  make clean                - Remove build artifacts"

install-node-modules:
	@echo "Installing Node dependencies..."
	@if [ -f "package.json" ]; then \
		npm install; \
		echo "✅ Node modules installed"; \
	else \
		echo "❌ package.json not found"; \
		exit 1; \
	fi

install-zola:
	@echo "Installing Zola 0.22.0..."
	@if command -v zola >/dev/null 2>&1; then \
		echo "Zola is already installed: $$(zola --version)"; \
	else \
		echo "Downloading Zola..."; \
		curl -L https://github.com/getzola/zola/releases/download/v0.22.0/zola-v0.22.0-x86_64-unknown-linux-gnu.tar.gz | tar xz; \
		sudo mv zola /usr/local/bin/; \
		echo "Zola installed: $$(zola --version)"; \
	fi

setup: install-node-modules install-zola
	@echo "✅ Setup complete!"

dev:
	npm run dev

build:
	npm run build

clean:
	rm -rf node_modules docs
