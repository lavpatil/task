def calculateDuration(start, end); {
    long elapsedTime = end - start

    Long second = (elapsedTime / 1000).longValue() % 60;
    Long minute = (elapsedTime / (1000 * 60)).longValue() % 60;
    Long hour = (elapsedTime / (1000 * 60 * 60)).longValue() % 24;
    Long remainderMillis = elapsedTime % 1000

    return "${hour}h ${minute}m ${second}s ${remainderMillis}ms"
}
