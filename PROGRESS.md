# Progress

## Foundations
- [x] Process vs thread anatomy (memory, stack, registers)
- [x] I/O-bound vs CPU-bound, and which tool fits each
- [x] GIL, concurrency vs parallelism
- [x] Preemptive (threading) vs cooperative (asyncio) multitasking

## Threading
- [x] `threading.Thread`: `start`, `join`, daemon threads
- [x] Return-value trap (shared dict + `Lock`)
- [x] `ThreadPoolExecutor`: `submit` + `as_completed`, `map`
- [ ] Thread-local storage (`threading.local`)
- [ ] `Lock` patterns and deadlocks
- [ ] `RLock`
- [ ] `Condition`: producer-consumer
- [ ] `Barrier`
- [ ] `Timer`
- [ ] Mini-challenge: bounded producer-consumer with `Lock` + `Condition`

## asyncio
- [x] Event loop mental model
- [x] Coroutine vs Task vs Future
- [x] Sequential `await` vs concurrent `gather`
- [x] Race conditions across `await` + `asyncio.Lock`
- [ ] `gather` vs `TaskGroup`
- [ ] `wait` and `wait_for`
- [ ] Cancellation and `shield`
- [ ] `Semaphore`, `Event`, `Queue`
- [ ] Running blocking code: `run_in_executor`, `to_thread`
- [ ] `async with` / `async for`
- [ ] Mini-challenge: rate-limited async scraper (`httpx` + `Semaphore`)

## Multiprocessing
- [ ] Process startup cost, `fork` vs `spawn`
- [ ] IPC: `Queue`, `Pipe`, `Value`/`Array`
- [ ] `Pool` vs `ProcessPoolExecutor`, `chunksize`
- [ ] `Manager`
- [ ] asyncio + `ProcessPoolExecutor`
- [ ] Mini-challenge: parallel image-processing pipeline

## Choosing the right tool
- [ ] Decision matrix
- [ ] Benchmarks for each workload type
- [ ] Design exercise: Django API with external APIs + ML + PostgreSQL

## Advanced
- [ ] `asyncio.Queue` multi-stage pipeline
- [ ] Structured concurrency and `ExceptionGroup`
- [ ] Free-threaded Python 3.13
- [ ] `contextvars`
- [ ] Profiling async code (`uvloop`, debug mode)

## Applied: FastAPI
- [x] Sync vs async endpoints under concurrent load
- [x] Dependency injection: `Depends`, `yield` dependencies
