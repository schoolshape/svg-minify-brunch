#!/usr/bin/env python

import sys, rsvg, os, svg_stack as ss

doc = ss.Document()
layout = ss.VBoxLayout()
dirs = os.walk(sys.argv[1])
cssfile = open(sys.argv[2], 'a')

height = 0
css_group = {}
first = True
last_svg_height = 0
for root, ds, fs in dirs:
    for f in fs:
        if root[4:10] != 'assets' and f[-4:] == '.svg':
            svg = rsvg.Handle(file=root+'/'+f)
            last_svg_height = svg.props.height
            if first:
                first = False
            else:
                height = height + last_svg_height/2.0
            css_group[f[:-4]] = height
            height = height + last_svg_height/2.0
            layout.addSVG(root + '/' + f, alignment = ss.AlignLeft)

doc.setLayout(layout)
doc.save(sys.argv[3])

height = height - last_svg_height/2.0
for name in css_group:
    css =  """
.{0} {{
  background-image: url(app.svg);
  background-size: 100%;
  background-position: 0% {1}%;
}}
""".format(name, css_group[name]/float(height) * 100)
    cssfile.write(css)
cssfile.close()
