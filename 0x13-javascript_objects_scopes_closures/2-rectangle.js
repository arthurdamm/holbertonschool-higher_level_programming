#!/usr/bin/node
// Checked Rectangle Class
class Rectangle {
  constructor (w, h) {
    if ((w = parseInt(w)) && w > 0 &&
        (h = parseInt(h)) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
