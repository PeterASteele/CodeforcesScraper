"use strict";



var fs = require('fs');
var f = fs.open('html.file', 'r');
var content = f.read();
var page = require('webpage').create();
page.viewportSize = { width: 3000, height : 5000 };
/*page.evaluate(function() {
    var el = document.getElementById('surface'),
        context = el.getContext('2d'),
        width = window.innerWidth,
        height = window.innerHeight,
        cx = width / 2,
        cy = height / 2,
        radius = width  / 2.3,
        imageData,
        pixels,
        hue, sat, value,
        i = 0, x, y, rx, ry, d,
        f, g, p, u, v, w, rgb;

    el.width = width;
    el.height = height;
    imageData = context.createImageData(width, height);
    pixels = imageData.data;

    for (y = 0; y < height; y = y + 1) {
        for (x = 0; x < width; x = x + 1, i = i + 4) {
            rx = x - cx;
            ry = y - cy;
            d = rx * rx + ry * ry;
            if (d < radius * radius) {
                hue = 6 * (Math.atan2(ry, rx) + Math.PI) / (2 * Math.PI);
                sat = Math.sqrt(d) / radius;
                g = Math.floor(hue);
                f = hue - g;
                u = 255 * (1 - sat);
                v = 255 * (1 - sat * f);
                w = 255 * (1 - sat * (1 - f));
                pixels[i] = [255, v, u, u, w, 255, 255][g];
                pixels[i + 1] = [w, 255, 255, v, u, u, w][g];
                pixels[i + 2] = [u, u, w, 255, 255, v, u][g];
                pixels[i + 3] = 255;
            }
        }
    }

    context.putImageData(imageData, 0, 0);
    document.body.style.backgroundColor = 'white';
    document.body.style.margin = '0px';
});*/


page.content = content;

page.onError = function(msg, trace) {

  var msgStack = ['ERROR: ' + msg];

  if (trace && trace.length) {
    msgStack.push('TRACE:');
    trace.forEach(function(t) {
      msgStack.push(' -> ' + t.file + ': ' + t.line + (t.function ? ' (in function "' + t.function +'")' : ''));
    });
  }

  console.error(msgStack.join('\n'));

};
page.render("problem-statement.png");


phantom.exit();
