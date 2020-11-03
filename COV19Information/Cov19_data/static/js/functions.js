function get_time(){
			$.ajax({
				url:"/time",
				timeout:10000,
				success:function(data){
					$("#time").html("EDT "+data)
				},
				error:function(xhr,type,errorThrown){

				}
			});
		}

function get_c1_data(){
    $.ajax({
        url:"/c1",
        success:function(data){
            $(".num h1").eq(0).text(data.confirmed);
            $(".num h1").eq(1).text(data.recovered);
            $(".num h1").eq(2).text(data.dead);
            $(".num h1").eq(3).text(data.fatality_rate);
        },
        error:function(xhr,type,errorThrown){

        }
    })
}

function get_c2_data(){
    $.ajax({
        url:"/c2",
        success:function(data){
            ec_center_option.series[0].data=data.data
            ec_center.setOption(ec_center_option)
        },
        error:function(xhr,type,errorThrown){

        }

    })
}

function get_l1_data(){
    $.ajax({
        url:"/l1",
        success:function(data){
            ec_left1_Option.xAxis[0].data=data.day
            ec_left1_Option.series[0].data=data.confirmed
            ec_left1_Option.series[1].data=data.recovered
            ec_left1_Option.series[2].data=data.dead
            ec_left1.setOption(ec_left1_Option)
        },
        error:function(xhr,type,errorThrown){

        }

    })
}

function get_l2_data(){
    $.ajax({
        url:"/l2",
        success:function(data){
            ec_left2_Option.xAxis[0].data=data.day
            ec_left2_Option.series[0].data=data.confirmed_add
            ec_left2_Option.series[1].data=data.dead_add
            ec_left2.setOption(ec_left2_Option)
        },
        error:function(xhr,type,errorThrown){

        }

    })
}

function get_r1_data() {
    $.ajax({
        url: "/r1",
        success: function (data) {
            ec_right1_option.xAxis[0].data=data.state;
            ec_right1_option.series[0].data=data.confirmed;
            ec_right1.setOption(ec_right1_option);
        }
    })
}

function get_r2_data() {
    $.ajax({
        url: "/r2",
        success: function (data) {
            ec_right2_option.series[0].data=data.kws;
            ec_right2.setOption(ec_right2_option);
        }
    })
}


get_time()
get_c1_data()
get_c2_data()
get_l1_data()
get_l2_data()
get_r1_data()
get_r2_data()
setInterval(get_time, 1000*60)
setInterval(get_c1_data, 1000*60*60*12)
setInterval(get_c2_data, 1000*60*60*12)
setInterval(get_l1_data, 1000*60*60*12)
setInterval(get_l2_data, 1000*60*60*12)
setInterval(get_r1_data, 1000*60*60*12)
setInterval(get_r2_data, 1000*7)