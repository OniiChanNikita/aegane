window.onload=function() {
    document.body.classList.add('loaded_hiding');
    window.setTimeout(function () {
      document.body.classList.add('loaded');
      document.body.classList.remove('loaded_hiding');
    }, 500);
    paralax = document.querySelector(".parallax")
    if (paralax) {
        /*parallax content*/
        const body = document.querySelector('body');
        const main_content = document.querySelector('.content')
        const content = document.querySelector('.parallax_container')
        const house = document.querySelector('.house-parallax');
        const up = document.querySelector('.up-parallax');
        const down = document.querySelector('.down-parallax');
        const center_label = document.querySelector('#_cl')
        const right_label = document.querySelector('#_rl');
        const left_label = document.querySelector('#_ll');
        const all_labels = document.querySelector('.parallax_flex')
        const logo_profile = document.querySelector('.logo_main_nav')
        const airplane = document.querySelector('.airplane')
        const tourists = document.querySelector('.tourists')


        const speed = 0.1;
        const forAround = 90;
        const forUp = 70;
        const forDown = 60;

        let positionX = 0, positionY = 0;
        let coordXprocent = 0, coordYprocent = 0;

        function SetMouseParalaxStyle() {
            const distX = coordXprocent - positionX;
            const distY = coordYprocent - positionY;

            positionX = positionX + (distX * speed);
            positionY = positionY + (distY * speed);


            house.style.cssText = `transform: translate(${positionX / forAround}%,${positionY / forAround}%);`;
            up.style.cssText = `transform: translate(${positionX / forUp}%,${positionY / forUp}%);`;
            down.style.cssText = `transform: translate(${positionX / forDown}%,${positionY / forDown}%);`;
            requestAnimationFrame(SetMouseParalaxStyle);
        }

        SetMouseParalaxStyle();

        paralax.addEventListener("mousemove", function (e) {
            const parallaxWidth = paralax.offsetWidth;
            const parallaxHeight = paralax.offsetHeight;

            const coordX = e.pageX - parallaxWidth / 2;
            const coordY = e.pageY - parallaxHeight / 2;

            coordXprocent = coordX / parallaxWidth * 100;
            coordYprocent = coordY / parallaxHeight * 100;
        });
        function parallaxFunc(scrollTopProcent, scrollTopProcentOpacity) {
            let scrollPercent = ((window.pageYOffset || document.documentElement.scrollTop) / ((document.documentElement.scrollHeight) - (window.innerHeight))) * 100;
            tourists.style.cssText = `left: ${Math.pow(5, 250/scrollPercent)}px`

            if (scrollPercent >= 25){
                airplane.style.cssText = `margin-bottom: ${Math.pow(scrollPercent/10, 2)}px`; /*opacity: ${scrollPercent/90};*/
                airplane.style.transform = 'scale(' + (90 / Math.pow(scrollPercent/10, 2)) + ')';
                /*airline_airplane.style.cssText = `opacity: ${(scrollPercent/90) }`;*/
            }
            if (scrollTopProcent>=1.0){

                /*house.parentElement.style.cssText = `display: none;`
                up.parentElement.style.cssText = `display: none;`
                down.parentElement.style.cssText = `display: none;`*/
                center_label.parentElement.style.cssText = `display: none;`
                right_label.parentElement.style.cssText = `display: none;`
                left_label.parentElement.style.cssText = `display: none;`
            }else{
                house.parentElement.style.cssText = `filter: blur(${1/scrollTopProcentOpacity}px); z-index: 2; display: block;`;
                up.parentElement.style.cssText = `filter: blur(${1/scrollTopProcentOpacity}px); z-index: 0; display: block;`;
                down.parentElement.style.cssText = `filter: blur(${1/scrollTopProcentOpacity}px); z-index: 3; display: block;`;
                if (scrollTopProcent>=0.5){
                    center_label.parentElement.style.cssText = `margin: -${scrollTopProcent*25}px 0; display: block;`;
                }
                right_label.parentElement.style.cssText = `margin: 0 0 0 ${scrollTopProcent*200}px; display: block;`;
                left_label.parentElement.style.cssText = `margin: 0 ${scrollTopProcent*200}px 0 0; display: block;`;
                all_labels.parentElement.style.cssText = `bottom: ${scrollTopProcent*150}px; display: block;`
                main_content.style.cssText = `display: block; opacity: ${1/scrollTopProcentOpacity*2}`;
                logo_profile.style.cssText = `opacity: ${scrollTopProcentOpacity}`;

            }
        }
        window.addEventListener('scroll', function () {
            const scrollTopProcentOpacity = paralax.offsetHeight / body.scrollTop / 2.5;
            const scrollTopProcent = body.scrollTop / paralax.offsetHeight;
            parallaxFunc(scrollTopProcent, scrollTopProcentOpacity);
        });
        /*end parallax content*/



        /*slider photo*/
        const images = document.querySelectorAll('.slider_status img')
        const sliderLine = document.querySelector('.slider_status')
        let count = 0;
        let width;

        function init(){
            let width = document.querySelector('.slider_body').offsetWidth;
            sliderLine.style.width = `${width*images.length}px`;
            images.forEach(item => {
                item.style.width = width + "px";
                item.style.height = "auto";
            });

        }
        window.addEventListener('resize', init);
        init();
        document.querySelector(".status_right").addEventListener('click', function (){
            count++;
            if (count === images.length){
                count = 0;
            }
            sliderLine.style.transform = `translate(-${count*width}px)`;
        });
        document.querySelector(".status_left").addEventListener('click', function (){
            count--;
            if (count === -1){
                count = images.length - 1;
            }
            sliderLine.style.transform = `translate(-${count*width}px)`;
        });
    }
}