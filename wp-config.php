<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://codex.wordpress.org/Editing_wp-config.php
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'campusnutrition' );

/** MySQL database username */
define( 'DB_USER', 'root' );

/** MySQL database password */
define( 'DB_PASSWORD', '' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         '7m1QQ34>K*Ld&YLAZNS:t7gN Y)|[ip_5 +Y[?XczR+Jdv~#*ZFd>ha0vS!y`Mds' );
define( 'SECURE_AUTH_KEY',  ' Q6sj#(}Hi;WUh#Xxd=JpCcfi(J0U.8p*JH~AT-3RJhID_s ~Fl]OQ9?;-Npkt`u' );
define( 'LOGGED_IN_KEY',    '|6GD;j0+?bCq9xVr#}}r-}0Fr}/;V,lp`[iWhhUp7Yp<9RKgz04T+NDq(UyRR0VC' );
define( 'NONCE_KEY',        '7LHPI@.[16za[*q*0AO.vQ].JqPuc%ENf.WeIgP_Y]</}6g_0ZaFlC<L9[aT.X@m' );
define( 'AUTH_SALT',        '?UY,@=U.:F:i*:5XrUG08Z9(uM6CO%fT-WaYM(Upz?}Mkh:p{4,at2}hl~zyP$81' );
define( 'SECURE_AUTH_SALT', 'uBZ@F$6Ui67Ki^YPKK`Zdn4O{OYsJ0px9[r}mW0 B3xY[ZKOoXp|u5O]]}DLIZ=[' );
define( 'LOGGED_IN_SALT',   'pg_?5#BDgzO}%+|08|5GMb8y3Gf0gix_k*IJj7p4ZAW^L5Fc;ZLiL P ,FQ>1$-!' );
define( 'NONCE_SALT',       '{s&q@:jrbHT0J:|@QU0PYC)opC]b1:Uj5G8Zo+R)XkONOq{nHY8eW$K1`_HEE@:J' );

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the Codex.
 *
 * @link https://codex.wordpress.org/Debugging_in_WordPress
 */
define( 'WP_DEBUG', false );

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', dirname( __FILE__ ) . '/' );
}

/** Sets up WordPress vars and included files. */
require_once( ABSPATH . 'wp-settings.php' );
