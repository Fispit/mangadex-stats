function makeResponsive(){

var navbar_elems=d3.select("navbar").select("a");

navbar_elems.selectAll().on("mouseover",function () {d3.select(this).attr("fill","#ff6740")})

}

makeResponsive()