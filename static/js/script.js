// java script file

function main() {

}

// onClick
function onClickFacebook() {
	alert("login with facebook feature is coming soon");
}

function onClickGmail() {
	alert("login with Gmail feature is coming soon");
}

$('li.dropdown').hover(function() {
  $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeIn(500);
}, function() {
  $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeOut(500);
});

main();
