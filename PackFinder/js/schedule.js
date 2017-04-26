Array.prototype.remove = function() {
    var what, a = arguments, L = a.length, ax;
    while (L && this.length) {
        what = a[--L];
        while ((ax = this.indexOf(what)) !== -1) {
            this.splice(ax, 1);
        }
    }
    return this;
};
var sClickColor = "rgb(61, 141, 176)";
var selected = [];
function changeColor(n) {
    if (n) {
        sClickColor = "rgb(61, 141, 176)";
    } else if (n == false) {
        sClickColor = "rgb(255, 251, 166)";
    } else {
        sClickColor = "rgba(224, 72, 72, 0.77)";
    }
}
[].forEach.call(document.getElementsByTagName('td'), function(item) {
    item.addEventListener('click', function() {
        if (item.className != "hour") {
            if (selected.includes(item.id)) {
                selected.remove(item.id);
                item.style.backgroundColor = "c8cdd4";
            } else {
                item.style.backgroundColor = sClickColor;
                selected.push(item.id);
            }
        }
    }, false);
});

$(document).ready(function(){
	var my_posts = $("[rel=tooltip]");

	var size = $(window).width();
	for(i=0;i<my_posts.length;i++){
		the_post = $(my_posts[i]);

		if(the_post.hasClass('invert') && size >=767 ){
			the_post.tooltip({ placement: 'left'});
			the_post.css("cursor","pointer");
		}else{
			the_post.tooltip({ placement: 'rigth'});
			the_post.css("cursor","pointer");
		}
	}
});

function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ob)
{
    ob.dataTransfer.setData("Text",ob.target.id);
}

function drop(ob)
{
    var id = ob.dataTransfer.getData("Text");
    var t = ob.target;
    if (ob.target.nodeName == "IMG")
        t = ob.target.parentNode;
    t.innerHTML = "";
    var img = document.getElementById(id);
    t.appendChild(img);
    $('#images').append(img.src + "; " )
    ob.preventDefault();
}

$(function() {
    $("#draggable").draggable({
        revert:  function(dropped) {
             var $draggable = $(this),
                 hasBeenDroppedBefore = $draggable.data('hasBeenDropped'),
                 wasJustDropped = dropped && dropped[0].id == "droppable";
             if(wasJustDropped) {
                 // don't revert, it's in the droppable
                 return false;
             } else {
                 if (hasBeenDroppedBefore) {
                     // don't rely on the built in revert, do it yourself
                     $draggable.animate({ top: 0, left: 0 }, 'slow');
                     return false;
                 } else {
                     // just let the build in work, although really, you could animate to 0,0 here as well
                     return true;
                 }
             }
        }
    });

    $("#droppable").droppable({
        activeClass: 'ui-state-hover',
        hoverClass: 'ui-state-active',
        drop: function(event, ui) {
            $(this).addClass('ui-state-highlight').find('p').html('Dropped!');
            $(ui.draggable).data('hasBeenDropped', true);
        }
    });
});
