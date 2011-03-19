$(document).ready(function(){
	function hide($box, speed){
		$box.children(':not(label)').hide(speed);
	}
	function set($elm){
		var $label = $elm.children('label');
		hide($elm, $label);
		$label.css("cursor", "pointer");
		$label.toggle(function(){
			$elm.children(':not(style,script,textarea)').show('fast');
			//$elm.children(':not(style,script)').show('fast');
		}, function(){
			hide($elm, 'fast');
		});
	}
	var $stylesheet = $('label[for=id_stylesheet]').parents("p");
	var $javascript = $('label[for=id_javascript]').parents("p");
	set($stylesheet);
	set($javascript);
});