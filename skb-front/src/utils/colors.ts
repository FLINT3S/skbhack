export function blendColor(c: number[], n: number, i: number, d: number) {
  for (i = 3; i--; c[i] = d < 0 ? 0 : d > 255 ? 255 : d | 0) d = c[i] + n;
  return c
}

export function blendRGB(rgb: string, n: number) {
  return 'rgb(' + blendColor(rgb.match(/\d+/g)!.map(Number), n, 0, 0) + ')'
}
