const fibonacci = (num) => {
    let n1 = 0, n2 = 1, nextNum;
    if (num === 0) {
        return 0;
    }
    for (let i = 1; i < num; i++) {
        nextNum = n1 + n2;
        n1 = n2;
        n2 = nextNum;
    }
    return nextNum;
}

module.exports = {fibonacci}
