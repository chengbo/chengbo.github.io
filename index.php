<?php get_header(); ?>
<?php get_sidebar(); ?>

    <div id="articles" role="main">
        <?php if ( have_posts() ) : ?>

            <?php ?>
            <?php while ( have_posts() ) : the_post(); ?>
                <?php get_template_part( 'content', get_post_format() ); ?>
            <?php endwhile; ?>

        <?php else : ?>

            <article id="post-0">

            <?php if ( current_user_can( 'edit_posts' ) ) : ?>
                <header>
                    <h1>No posts to display</h1>
                </header>

                <div>
                    <p><?php printf(  'Ready to publish your first post? <a href="%s">Get started here</a>.', admin_url( 'post-new.php' ) ); ?></p>
                </div>

            <?php else : ?>
                <header>
                    <h1>Nothing Found</h1>
                </header>

                <div>
                    <p>Apologies, but no results were found. Perhaps searching will help find a related post.</p>
                    <?php get_search_form(); ?>
                </div>
            <?php endif; ?>

            </article>

        <?php endif; ?>
    </div>

<?php get_footer(); ?>