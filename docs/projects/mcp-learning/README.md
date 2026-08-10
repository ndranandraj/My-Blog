# Learning Track: MCP, from consumer to author

**Owner:** Anand
**Created:** July 2026
**Goal:** be able to design, build, test and ship an MCP server, ending with one
that serves this blog's own TN 2026 election data.

Separate from `docs/projects/mospi-mcp/`, which is a benchmark project with a
blog post as its deliverable. This one has a working server as its deliverable.
They share Rungs 1 to 4, so run them in parallel and get double value from the
same hours.

---

## The honest framing

The MCP protocol itself is small. You will absorb the spec in about an hour and
it is not where the difficulty lives. The difficulty is in **tool design**: how do
you shape a set of tools so that a language model cannot use them wrong?

That is a genuinely unsolved design problem, and the MoSPI server is a good place
to watch a competent team's answer to it. That is why this track is built around
reading their code before writing your own.

---

## Rung 1: Use one (1 hour)

Adding a connector is a config step, not a skill. Do it, but do not mistake it for
learning. The value here is noticing what a good and bad tool feel like from the
client side.

- [ ] Connect `https://mcp.mospi.gov.in/` to Claude
- [ ] Run the 15 queries from `docs/projects/mospi-mcp/BENCHMARK-CHECKLIST.md`
- [ ] Note every point where the model guessed wrong, and ask why the tool let it

**You learn:** what tool descriptions are for, why parameter naming matters, what
a four-step forced workflow feels like when you are on the receiving end.

---

## Rung 2: Read a good one (2 hours)

```bash
git clone https://github.com/nso-india/esankhyiki-mcp.git
```

Read in this order:

1. `mospi_server.py`, the tool definitions and their docstrings
2. `swagger/`, one YAML, to see validation driven by spec rather than hardcoded
3. `mospi/client.py`, the HTTP layer
4. `tests/`, how they test 25 datasets in-process with no server running
5. `observability/telemetry.py`, OpenTelemetry middleware

Things to look for specifically:

- [ ] **Docstrings are written for an LLM, not a human.** Note the difference.
- [ ] **Enforced sequencing.** `get_indicators` refuses to be useful until
      `get_metadata` has run. Why did they need that, and what would break without it?
- [ ] **Auto-routing.** CPI picks the Group or Item endpoint based on filters. The
      model never learns that distinction exists.
- [ ] **The injected rules block.** Copy the verbatim strings. This is the single
      most interesting design decision in the repo and it is also the material for
      the governance section of the benchmark post.
- [ ] **Swagger as source of truth.** Params validated against YAML, not constants.

**You learn:** the actual craft. This rung is where MCP clicks.

---

## Rung 3: Run one locally and watch it work (1 hour)

```bash
cd esankhyiki-mcp
pip install -r requirements.txt
fastmcp run mospi_server.py:mcp --transport http --port 8000
```

Or the full stack with tracing:

```bash
docker-compose up -d
# MCP server: http://localhost:8000/mcp
# Jaeger UI:  http://localhost:16686
```

Then point Claude at your local instance:

```bash
claude mcp add esankhyiki-local --transport http http://localhost:8000/mcp
```

- [ ] Run a query against local, confirm same answer as hosted
- [ ] Open Jaeger and read the trace for one query
- [ ] Count the actual API round trips behind one natural-language question
- [ ] Break something on purpose (bad filter code) and watch the error path
- [ ] Run their pytest suite: `pytest tests/ -v -p no:anyio`

**You learn:** what is really happening under a tool call, and why observability
matters once a model is driving your API instead of a human.

---

## Rung 4: Contribute to one (an afternoon)

Their `CONTRIBUTING.md` documents adding a new dataset. It is a well-scoped first
PR against a government repository.

- [ ] Pick a dataset MoSPI publishes that is not among the 25
- [ ] Write the Swagger spec
- [ ] Wire the client, add tests
- [ ] Open the PR
- [ ] Separately, file issues for any bugs the benchmark turned up

**You learn:** the shape of a real MCP codebase from the inside, plus a line in the
benchmark post that says you shipped to it rather than only reviewing it.

---

## Rung 5: Build your own (the real curve)

**Deliverable: an MCP server for the TN 2026 election data.**

Full sketch in `TN-ELECTION-MCP-PLAN.md` in this folder. Summary: 13 JSON sidecars
already sit in `static/election-dashboard/data/`, about 1.3 MB total, covering 234
constituencies, 4,257 candidates, 2021 to 2026 swing, defeated incumbents, assembly
demographics and party efficiency. Wrapping them is roughly 200 to 300 lines of
FastMCP.

Nobody has built an Indian election MCP server. It makes the dataset usable in a
way a CSV download never is, and it is a second blog post.

- [ ] Milestones tracked in `TN-ELECTION-MCP-PLAN.md`

**You learn:** everything, because now the design decisions are yours and there is
no reference implementation to lean on.

---

## Rung 6 (optional): the delimitation tool

Once Rung 5 ships, the delimitation scenario engine from
`docs/projects/` becomes an obvious second server: expose apportionment methods,
house sizes and census years as tools, so anyone can ask an assistant to run a
scenario. That is a genuinely novel artifact and it links the two projects.

---

## Time budget

| Rung | Time | Blocking? |
|:---|:---|:---|
| 1. Use | 1 hr | No, shared with benchmark project |
| 2. Read | 2 hr | Do before Rung 5 |
| 3. Run local | 1 hr | No |
| 4. Contribute | 4 hr | Optional, but high value for the post |
| 5. Build | 8-12 hr | The main event |

Realistically two weekends if you want the TN server shipped.

---

## What to skip

- Reading the MCP spec end to end before doing anything. Skim it, then read code.
- Building a toy weather server from a tutorial. You have real data. Use it.
- Worrying about transports. Use HTTP for remote, stdio for local, move on.
