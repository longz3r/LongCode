Blockly.Blocks['control_if'] = {
    init: function() {
      this.appendValueInput("if")
          .setCheck("Boolean")
          .appendField("Nếu");
      this.appendStatementInput("then")
          .setCheck("Boolean")
          .setAlign(Blockly.ALIGN_RIGHT)
          .appendField("thực hiện");
      this.setInputsInline(false);
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(180);
   this.setTooltip("Câu lệnh điều kiện");
    }
  };

Blockly.Python['control_if'] = function(block) {
    var ditmemay = "Dit me may Minh Duy"
    return ditmemay
}