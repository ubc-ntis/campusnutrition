


<div class="blog-post">

<h2 class="blog-post-title"><?php the_title(); ?></h2>
<p class="blog-post-meta"><?php the_date(); ?> by <a href="#"><?php the_author(); ?></a></p>

<h2 class="blog-post-title"><?php the_title(); ?></h2>
<p class="blog-post-meta"><?php the_date(); ?> by <a href="#"><?php the_author(); ?></a></p>

<div class="box">
<a class="button" href="#popup1">Let me Pop up</a>
</div>

<div id="popup1" class="overlay">
    <div class="popup">
        <h2>Here i am</h2>
            <a class="close" href="#">&times;</a>
        <div class="content">
        Thank to pop me out of that button, but now i'm done so you can close this window.
    </div>
</div>
</div>
<?php the_content(); ?>

</div><!-- /.blog-post -->