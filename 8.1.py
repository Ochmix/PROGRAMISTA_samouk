import statistics
yolo = [1, 3, 5, 3, 4, 7, 8, 9, 11, 45, 33, 115]
print(statistics.mean(yolo))
print(statistics.fmean(yolo))
print(statistics.geometric_mean(yolo))
print(statistics.harmonic_mean(yolo))
print(statistics.median(yolo))
print(statistics.median_low(yolo))
print(statistics.median_high(yolo))
print(statistics.median_grouped(yolo))
print(statistics.mode(yolo))
print(statistics.multimode(yolo))
print(statistics.quantiles(yolo))

