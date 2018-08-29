$.get( "https://raw.githubusercontent.com/WarcraftPriests/bfa-shadow-priest/master/json_Charts/wowhead_test.txt", function( data ) {
			$("body").append(data)
});