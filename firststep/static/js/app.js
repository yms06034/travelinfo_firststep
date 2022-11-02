new Swiper(".swiper-container", {
  spaceBetween: 30,
  centeredSlides: true,
  loop: true,
  autoplay: {
    delay: 3000,
    disableOnInteraction: false,
  },
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});

var mainCity = document.querySelector('#main_city');

mainCity.onchange = () => {
  var subCity = document.querySelector('#sub_city');
  var mainOption = mainCity.options['mainCity.selectedIndex'].innerText;
}

var subOptions = {
  seoul : {seoul},
  busan : {busan},
  daegu : {daegu},
  incheon : {incheon},
  gwangju : {gwangju},
  daejeon : {daejeon},
  uisan : {uisan},
  sejong : {sejong},
  gyepnggido : {gyepnggido},
  gangwon : {gangwon},
  chungnam : {chungnam},
  chungbuk : {chungbuk},
  jeonam : {jeonam},
  jeobuk : {jeobuk},
  gyeongnam : {gyeongnam},
  gyeongbuk : {gyeongbuk},
  jeju : {jeju}
}

switch (mainOption) {
  case '서울' :
    var subOptions = subOptions.seoul;
    break
  case '부산' :
    var subOptions = subOptions.busan;
    break
  case '대구' :
    var subOptions = subOptions.daegu;
    break
  case '인천' :
    var subOptions = subOptions.incheon;
    break
  case '광주' :
    var subOptions = subOptions.gwangju;
    break
  case '대전' :
    var subOptions = subOptions.daejeon;
    break
  case '울산' :
    var subOptions = subOptions.uisan;
    break
  case '세종' :
    var subOptions = subOptions.sejong;
    break
  case '경기' :
    var subOptions = subOptions.gyepnggido;
    break
  case '강원' :
    var subOptions = subOptions.gangwon;
    break
  case '충남' :
    var subOptions = subOptions.chungnam;
    break
  case '충북' :
    var subOptions = subOptions.chungbuk;
    break
  case '전남' :
    var subOptions = subOptions.jeonam;
    break
  case '전북' :
    var subOptions = subOptions.jeobuk;
    break
  case '경남' :
    var subOptions = subOptions.gyeongnam;
    break
  case '경북' :
    var subOptions = subOptions.gyeongbuk;
    break
  case '제주' :
    var subOptions = subOptions.jeju;
    break
}

subCity.options.length = 0;

for (var i = 0; i < subOptions.length; i++) {
  var option = document.createElement('option');
  option.innerText = subOptions[i];
  subCity.append(option);
}