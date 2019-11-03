/**
 * @param {Number} min 下限 （闭区间）
 * @param {Number} max 上限 （开区间）
 * @return [min. max]范围的随机整数
 */
function randomInt(min, max) {
	return parseInt(Math.random() * (max - min)) + min
}