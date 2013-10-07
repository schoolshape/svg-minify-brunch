fs = require('fs')

module.exports = class SVGMINIFY
  brunchPlugin: yes

  constructor: (@config) ->
    null
 
  onCompile: (changeFiles) ->
    #fs.
    console.log changeFiles
