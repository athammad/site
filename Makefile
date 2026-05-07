.PHONY: all site cv slides posts pages clean preview

# Render everything except the broken notebook post
all: cv slides pages

# Full site render (will fail if Data Science project Boilerplate.qmd is broken)
site:
	quarto render

# Render CV page only
cv:
	quarto render cv/cv.qmd

# Render slides listing page and copy slide HTML files to docs/
slides:
	quarto render slides.qmd
	cp -r slides/. docs/slides/

# Render all non-notebook top-level pages
pages:
	quarto render index.qmd
	quarto render about.qmd
	quarto render papers.qmd
	quarto render students.qmd
	quarto render teaching.qmd
	quarto render posts.qmd
	quarto render gallery.qmd
	quarto render solutions.qmd
	quarto render toolkits.qmd
	quarto render research.qmd

# Render blog posts (may fail on Data Science project Boilerplate.qmd)
posts:
	@for f in posts/*.qmd; do \
		echo "Rendering $$f..."; \
		quarto render "$$f" 2>&1 | tail -1 || echo "  FAILED: $$f"; \
	done

# Start local preview server
preview:
	quarto preview

clean:
	rm -rf docs/ _freeze/
