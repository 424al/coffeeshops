const navSlide = () => {

	const burger = document.querySelector('.burger');
	const nav = document.querySelector('.nav-items');
	const navLinks = document.querySelectorAll('.nav-items li')
	//toggle nav
	burger.addEventListener('click',() => {
		//Toggle Nav
		nav.classList.toggle('nav-active');
		burger.classList.toggle('.toggle');
	});
	//Animate links
}
navSlide();