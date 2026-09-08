export function number(busStops: [number, number][]): number {
  return busStops.reduce((total, [on, off]) => total + on - off, 0);
}