# Proof branch only: sum an xtrace (PS4 '+ $EPOCHREALTIME file:line ') by line.
import re, sys, collections
ev = sorted((float(m.group(1)), m.group(2), m.group(3)[:90])
            for l in open(sys.argv[1], errors="replace")
            for m in [re.match(r"^\++ (\d+\.\d+) (\S+) (.*)", l)] if m)
by = collections.Counter(); ex = {}
for a, b in zip(ev, ev[1:]):
    by[a[1]] += b[0] - a[0]; ex.setdefault(a[1], a[2])
print(f"PROFILE   traced {(ev[-1][0] - ev[0][0]) * 1000:.0f} ms")
for k, v in by.most_common(6):
    print(f"PROFILE   {v * 1000:6.0f} ms {k:28} {ex[k]}")
