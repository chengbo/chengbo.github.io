
    <article id="post-<?php the_ID(); ?>">
        <header>
            <?php the_post_thumbnail(); ?>
            <?php if ( is_single() ) : ?>
            <h1><?php the_title(); ?></h1>
            <?php else : ?>
            <h1>
                <a href="<?php the_permalink(); ?>" title="<?php echo esc_attr( sprintf( 'Permalink to %s', the_title_attribute( 'echo=0' ) ) ); ?>" rel="bookmark"><?php the_title(); ?></a>
            </h1>
            <?php endif; ?>
        </header>

        <?php if ( is_search() ) : ?>
        <div>
            <?php the_excerpt(); ?>
        </div>
        <?php else : ?>
        <div>
            <?php the_content( 'Continue reading &rarr;' ); ?>
        </div>
        <?php endif; ?>

        <footer>
            <?php edit_post_link(); ?>
        </footer>
    </article>
