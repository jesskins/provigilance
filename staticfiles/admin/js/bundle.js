/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/******/ 	var __webpack_modules__ = ({

/***/ "./static/scripts.js":
/*!***************************!*\
  !*** ./static/scripts.js ***!
  \***************************/
/***/ (() => {

eval("// Ensure the document is ready\n$(document).ready(function () {\n  // Initialize jQuery UI Datepicker on the calendar element\n  $(\"#calendar\").datepicker({\n    // Customize the datepicker options if needed\n  });\n\n  // Function to toggle search bar visibility\n  function toggleSearch() {\n    var searchBar = document.getElementById('searchBar');\n    if (searchBar.style.display === 'none' || searchBar.style.display === '') {\n      searchBar.style.display = 'block';\n    } else {\n      searchBar.style.display = 'none';\n    }\n  }\n\n  // Function to handle the request call back button\n  function requestCallBack() {\n    window.location.href = \"/request-callback/\";\n  }\n\n  // New functions for the footer\n  document.getElementById('toggle-theme').addEventListener('click', function () {\n    document.body.classList.toggle('dark-mode');\n  });\n  function scrollToTop() {\n    window.scrollTo({\n      top: 0,\n      behavior: 'smooth'\n    });\n  }\n  var form = document.getElementById('testimonial-form');\n  if (form) {\n    var inputs = form.querySelectorAll('input, select, textarea');\n    var clearFormButton = document.getElementById('clear-form');\n    if (inputs.length > 0 && clearFormButton) {\n      inputs.forEach(function (input) {\n        input.addEventListener('input', function () {\n          if (input.checkValidity()) {\n            input.classList.add('valid');\n          } else {\n            input.classList.remove('valid');\n          }\n        });\n      });\n      clearFormButton.addEventListener('click', function () {\n        clearFormButton.classList.add('clicked');\n        form.reset();\n        inputs.forEach(function (input) {\n          input.classList.remove('valid');\n          if (input.type !== 'file') {\n            input.value = '';\n          }\n        });\n        form.querySelectorAll('select').forEach(function (select) {\n          return select.selectedIndex = 0;\n        });\n        setTimeout(function () {\n          clearFormButton.classList.remove('clicked');\n        }, 500);\n      });\n    }\n  }\n});\n\n//# sourceURL=webpack:///./static/scripts.js?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__["./static/scripts.js"]();
/******/ 	
/******/ })()
;