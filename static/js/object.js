const screenObject = document.querySelector("#screen");
const screenList = document.querySelector("#screen_list");
const randomObject = document.querySelector("#random");
const randomList = document.querySelector("#random_list");
const groupObject = document.querySelector("#group");
const groupList = document.querySelector("#group_list");

const HIDDEN_CLASSNAME = "hidden";

function onMouseScreen(event) {
  event.preventDefault();
  screenList.classList.remove(HIDDEN_CLASSNAME);
}

function onMouseRandom(event) {
  event.preventDefault();
  randomList.classList.remove(HIDDEN_CLASSNAME);
}

function onMouseGroup(event) {
  event.preventDefault();
  groupList.classList.remove(HIDDEN_CLASSNAME);
}

function outMouseScreen(event) {
  event.preventDefault();
  screenList.classList.add(HIDDEN_CLASSNAME);
}

function outMouseRandom(event) {
  event.preventDefault();
  randomList.classList.add(HIDDEN_CLASSNAME);
}

function outMouseGroup(event) {
  event.preventDefault();
  groupList.classList.add(HIDDEN_CLASSNAME);
}

screenObject.addEventListener("mouseover", onMouseScreen);
screenList.addEventListener("mouseover", onMouseScreen);
randomObject.addEventListener("mouseover", onMouseRandom);
randomList.addEventListener("mouseover", onMouseRandom);
groupObject.addEventListener("mouseover", onMouseGroup);
groupList.addEventListener("mouseover", onMouseGroup);

// screenObject.addEventListener("mouseout",outMouseScreen);
screenList.addEventListener("mouseout", outMouseScreen);
// randomObject.addEventListener("mouseout",outMouseRandom);
randomList.addEventListener("mouseout", outMouseRandom);
// groupObject.addEventListener("mouseout",outMouseGroup)
groupList.addEventListener("mouseout", outMouseGroup);
