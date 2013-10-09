spawn = require('child_process').spawn

module.exports = class SVGMINIFY
  brunchPlugin: yes

  constructor: (@config) ->
    null
 
  onCompile: (changeFiles) ->
    spawn('svg/svg_minify.py',['app', 'target/app.css', 'target/app.svg'])
