#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const wid = 'X'.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(wid);
    }
  }

  rotate () {
    const temp = this.height
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}

module.exports = Rectangle;
