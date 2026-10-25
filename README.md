# async-python

Concurrency in Python (threading, asyncio and multiprocessing), worked
through hands-on in Python 3.13. I'm building this alongside my work as a
Python backend developer to deepen my understanding of what happens under
the hood.

## What this repo is
- Runnable Jupyter notebooks, one topic each, with timing benchmarks
  (`time.perf_counter`) that make the differences measurable
- Side-by-side comparisons: sync vs threaded vs async on the same workload
- Interview traps called out explicitly (`⚠️ INTERVIEW TRAP`) next to the
  code that shows them
- Small FastAPI experiments that show how these ideas behave in a real web
  server

## What's inside
| Area | Files |
|------|-------|
| Foundations | `1multitasking_basics.ipynb`: process vs thread, I/O-bound vs CPU-bound, preemptive vs cooperative |
| GIL & asyncio basics | `2asyncio_threading.ipynb`: GIL, concurrency vs parallelism, event loop, coroutine / Task / Future, `gather` |
| Threading | `threading/threading1.ipynb`: `Thread`, `start`/`join`/daemon, `ThreadPoolExecutor` with `submit` + `as_completed` and `map` |
| asyncio | `asyncio/race_cond_trap.ipynb`: race conditions across `await` points, fixed with `asyncio.Lock` |
| FastAPI | `examples/`: sync vs async endpoints under 300 concurrent requests; `fastapi/fastapi_depends.ipynb`: dependency resolution and `yield` dependencies |

See [PROGRESS.md](PROGRESS.md) for what's done and what's next.

## Running locally
    python -m venv .venv
    .venv\Scripts\activate          # Windows; use `source .venv/bin/activate` on macOS/Linux
    pip install -r requirements.txt

Open any notebook and select the `.venv` kernel.

To run the FastAPI sync vs async benchmark:

    fastapi dev examples/fast_main.py      # terminal 1
    python examples/async_client.py        # terminal 2

## Why it exists
Real backend work (Django, FastAPI, Celery, PostgreSQL) depends on knowing
what concurrency is actually doing. Why does a sync endpoint end up in a
threadpool? Why does one blocking call freeze the whole event loop? When is
a process pool worth what it costs to start? This repo is where I build that
intuition, one measured example at a time.
