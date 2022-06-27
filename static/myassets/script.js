

//NAVBAR SCROLL HIDE

var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
    var currentScrollPos = window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
        document.getElementById("navbar").style.top = "0";
    } else {
        document.getElementById("navbar").style.top = "-100px";
    }
    prevScrollpos = currentScrollPos;
}


//SCROLL REVEAL

window.sr = ScrollReveal();
sr.reveal('.navbar', {
    duration: 3000,
    origin: 'top',
    scale: 0.3
})

window.sr = ScrollReveal();
sr.reveal('.showcase-left', {
    duration: 2000,
    origin: 'top',
    distance: '300px',
    easing:'ease-out',
    opacity:0,
   /* rotate: {
        x: 20,
        z: 20
    }, */
    //scale:0.5,
    // reset:true
})

window.sr = ScrollReveal();
sr.reveal('.hero-h1', {
    duration: 2000,
    origin: 'right',
    distance: '700px',
    easing: 'ease-out',
    opacity:1, 
    // reset:true
})

window.sr = ScrollReveal();
sr.reveal('.h1-mute', {
    duration: 3000,
    origin: 'right',
    distance: '700px',
    easing: 'ease-out',
    opacity:0, 
    reset:true
})

window.sr = ScrollReveal();
sr.reveal('#ctaH1', {
    delay: 700,
    duration:1500,
    useDelay: 'onload',
    origin: 'left',
    distance: '300px',
    easing: 'ease-out',
    opacity:0, 
    viewfactor:1,
    viewOffset: {
        top: 220
    },
    reset:true
})

window.sr = ScrollReveal();
sr.reveal('#ctaButton', {
    delay: 700,
    duration:1500,
    useDelay: 'onload',
    origin: 'right',
    distance: '300px',
    easing: 'ease-out',
    opacity:0, 
    viewfactor:1,
    viewOffset: {
        top: 220
    },
    reset:true
})

window.sr = ScrollReveal();
sr.reveal('#card1', {
    duration:1500,
    origin: 'left',
    distance: '400px',
    easing: 'ease-out',
    opacity:0, 
    viewfactor:1,
    viewOffset: {
        top: 220
    },
    reset:true
})

window.sr = ScrollReveal();
sr.reveal('#card2', {
    duration:1500,
    origin: 'right',
    distance: '400px',
    easing: 'ease-out',
    opacity:0, 
    viewfactor:1,
    viewOffset: {
        top: 220
    },
    reset:true
})

window.sr = ScrollReveal();
sr.reveal('#card3', {
    duration:1500,
    origin: 'bottom',
    distance: '400px',
    easing: 'ease-out',
    opacity:0, 
    viewfactor:1,
    viewOffset: {
        top: 220
    },
    reset:true
})
window.sr = ScrollReveal();
sr.reveal('#card4', {
    duration:1500,
    delay:1500,
    origin: 'bottom',
    distance: '400px',
    easing: 'ease-out',
    opacity:0, 
    viewfactor:1,
    viewOffset: {
        top: 220
    },
    reset:true
})
window.sr = ScrollReveal();
sr.reveal('#card5', {
    duration:1500,
    delay:3000,
    origin: 'bottom',
    distance: '400px',
    easing: 'ease-out',
    opacity:0, 
    viewfactor:1,
    viewOffset: {
        top: 220
    },
    reset:true
})