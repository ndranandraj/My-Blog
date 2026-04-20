# Migrating PaperMod from a Git submodule to a Hugo Module

Run these commands **once** on your local machine, then commit and push.

## 1. Confirm prerequisites

```bash
hugo version   # must be extended, >= 0.140
go version     # any Go >= 1.22
```

## 2. Pull the theme as a module (generates go.sum and version-pins PaperMod)

```bash
cd /path/to/anand-blog
hugo mod get -u github.com/adityatelange/hugo-PaperMod
hugo mod tidy
```

This will:
- download PaperMod to `~/go/pkg/mod`
- pin the exact commit in `go.sum`
- update `go.mod` with the resolved version

## 3. Verify the build still works

```bash
hugo server -D
```

Open http://localhost:1313 — layout, fonts, and overrides should all still render.

## 4. Remove the legacy submodule

Once the module build is confirmed working in CI:

```bash
git rm --cached themes/PaperMod
git submodule deinit -f themes/PaperMod
rm -rf .git/modules/themes/PaperMod
rm -rf themes/PaperMod
rm .gitmodules
```

Then in `hugo.toml` delete the `theme = "PaperMod"` line and its comment block — the `[module.imports]` entry fully replaces it.

## 5. Update PaperMod in the future

```bash
hugo mod get -u github.com/adityatelange/hugo-PaperMod
hugo mod tidy
git add go.mod go.sum
git commit -m "Bump PaperMod"
```

No more `git submodule update --remote` dance.
