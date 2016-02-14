-- phpMyAdmin SQL Dump
-- version 3.1.2deb1ubuntu0.2
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 06-07-2010 a las 11:17:20
-- Versión del servidor: 5.0.75
-- Versión de PHP: 5.2.6-3ubuntu4.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `escuela`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administrativos`
--

CREATE TABLE IF NOT EXISTS `administrativos` (
  `id_administrativo` tinyint(4) NOT NULL auto_increment,
  `cargo` varchar(12) collate utf8_unicode_ci NOT NULL,
  `apellidos` varchar(30) collate utf8_unicode_ci NOT NULL,
  `nombres` varchar(40) collate utf8_unicode_ci NOT NULL,
  `calle` varchar(40) collate utf8_unicode_ci NOT NULL,
  `numero` varchar(6) collate utf8_unicode_ci NOT NULL,
  `localidad` varchar(30) collate utf8_unicode_ci NOT NULL,
  `telefono` varchar(16) collate utf8_unicode_ci NOT NULL,
  `celular` varchar(16) collate utf8_unicode_ci default NULL,
  `correo` varchar(64) collate utf8_unicode_ci default NULL,
  PRIMARY KEY  (`id_administrativo`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=4 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alumnos`
--

CREATE TABLE IF NOT EXISTS `alumnos` (
  `id_alumno` int(11) NOT NULL auto_increment,
  `apellidos` varchar(20) collate utf8_unicode_ci NOT NULL,
  `nombres` varchar(25) collate utf8_unicode_ci NOT NULL,
  `sexo` char(1) collate utf8_unicode_ci NOT NULL,
  `tipo_doc` varchar(3) collate utf8_unicode_ci NOT NULL,
  `num_doc` varchar(12) collate utf8_unicode_ci NOT NULL,
  `nacionalidad` char(2) collate utf8_unicode_ci NOT NULL,
  `fecha_nac` date NOT NULL,
  `lugar_nac` varchar(20) collate utf8_unicode_ci NOT NULL,
  `calle_dom` varchar(30) collate utf8_unicode_ci NOT NULL,
  `num_dom` varchar(5) collate utf8_unicode_ci NOT NULL,
  `piso_dom` varchar(2) collate utf8_unicode_ci default NULL,
  `dpto_dom` varchar(2) collate utf8_unicode_ci default NULL,
  `cp_dom` varchar(8) collate utf8_unicode_ci NOT NULL,
  `localidad_dom` varchar(25) collate utf8_unicode_ci NOT NULL,
  `pcia_dom` varchar(15) collate utf8_unicode_ci NOT NULL,
  `tel_dom` varchar(15) collate utf8_unicode_ci NOT NULL,
  `estudios` varchar(14) collate utf8_unicode_ci NOT NULL,
  `hasta_est` char(1) collate utf8_unicode_ci NOT NULL default '0',
  `correo` varchar(40) collate utf8_unicode_ci default NULL,
  `nombre_madre` varchar(30) collate utf8_unicode_ci default NULL,
  `tipo_doc_madre` varchar(3) collate utf8_unicode_ci default NULL,
  `num_doc_madre` varchar(8) collate utf8_unicode_ci default NULL,
  `nac_madre` char(2) collate utf8_unicode_ci default NULL,
  `fecha_nac_madre` date default NULL,
  `ocupacion_madre` varchar(30) collate utf8_unicode_ci default NULL,
  `vive_madre` tinyint(1) default NULL,
  `tel_contacto_madre` varchar(15) collate utf8_unicode_ci default NULL,
  `nombre_padre` varchar(30) collate utf8_unicode_ci default NULL,
  `tipo_doc_padre` varchar(3) collate utf8_unicode_ci default NULL,
  `num_doc_padre` varchar(8) collate utf8_unicode_ci default NULL,
  `nac_padre` char(2) collate utf8_unicode_ci default NULL,
  `fecha_nac_padre` date default NULL,
  `ocupacion_padre` varchar(30) collate utf8_unicode_ci default NULL,
  `vive_padre` tinyint(1) default NULL,
  `tel_contacto_padre` varchar(15) collate utf8_unicode_ci default NULL,
  `trat_medico` tinytext collate utf8_unicode_ci,
  `observaciones` tinytext collate utf8_unicode_ci,
  `jefe` tinyint(1) NOT NULL,
  `empleo` varchar(30) collate utf8_unicode_ci NOT NULL,
  `resp` varchar(10) collate utf8_unicode_ci NOT NULL default 'No aplica',
  `resp_esjefe` char(1) collate utf8_unicode_ci default NULL,
  `resp_nombre` varchar(65) collate utf8_unicode_ci default NULL,
  `resp_nac` char(2) collate utf8_unicode_ci default NULL,
  `resp_profesion` varchar(30) collate utf8_unicode_ci default NULL,
  `resp_condicion` varchar(30) collate utf8_unicode_ci default NULL,
  `resp_estudios` varchar(14) collate utf8_unicode_ci default NULL,
  `resp_hasta_estudios` char(1) collate utf8_unicode_ci default NULL,
  `resp_tipo_doc` varchar(3) collate utf8_unicode_ci default NULL,
  `resp_num_doc` varchar(12) collate utf8_unicode_ci default NULL,
  `resp_calle_dom` varchar(30) collate utf8_unicode_ci default NULL,
  `resp_num_dom` varchar(5) collate utf8_unicode_ci default NULL,
  `resp_piso_dom` varchar(2) collate utf8_unicode_ci default NULL,
  `resp_dpto_dom` varchar(2) collate utf8_unicode_ci default NULL,
  `resp_localidad_dom` varchar(25) collate utf8_unicode_ci default NULL,
  `resp_cp_dom` varchar(8) collate utf8_unicode_ci default NULL,
  `resp_te_dom` varchar(15) collate utf8_unicode_ci default NULL,
  `obra_social` varchar(30) collate utf8_unicode_ci default NULL,
  `num_afiliado` varchar(15) collate utf8_unicode_ci default NULL,
  `enfermedad` char(1) collate utf8_unicode_ci NOT NULL default '0',
  `enf_cual` varchar(30) collate utf8_unicode_ci default NULL,
  `internado` char(1) collate utf8_unicode_ci NOT NULL default '0',
  `int_por` varchar(30) collate utf8_unicode_ci default NULL,
  `alergia` char(1) collate utf8_unicode_ci NOT NULL default '0',
  `alergia_man` varchar(40) collate utf8_unicode_ci default NULL,
  `alergia_trat` char(1) collate utf8_unicode_ci NOT NULL default '0',
  `tratamiento` char(1) collate utf8_unicode_ci NOT NULL default '0',
  `trat_espec` varchar(30) collate utf8_unicode_ci default NULL,
  `quirurgico` char(1) collate utf8_unicode_ci NOT NULL default '0',
  `quir_edad` varchar(2) collate utf8_unicode_ci default NULL,
  `quir_tipo` varchar(30) collate utf8_unicode_ci default NULL,
  `limitacion` char(1) collate utf8_unicode_ci NOT NULL default '0',
  `limitacion_aclaracion` varchar(30) collate utf8_unicode_ci default NULL,
  `otros` varchar(60) collate utf8_unicode_ci default NULL,
  `institucion` varchar(50) collate utf8_unicode_ci default NULL,
  `institucion_dom` varchar(30) collate utf8_unicode_ci default NULL,
  `institucion_te` varchar(15) collate utf8_unicode_ci default NULL,
  `medico_apellido` varchar(30) collate utf8_unicode_ci default NULL,
  `medico_nombres` varchar(30) collate utf8_unicode_ci default NULL,
  `medico_dom` varchar(30) collate utf8_unicode_ci default NULL,
  `medico_te` varchar(15) collate utf8_unicode_ci default NULL,
  `familiar_apellido` varchar(30) collate utf8_unicode_ci default NULL,
  `familiar_nombres` varchar(30) collate utf8_unicode_ci default NULL,
  `familiar_dom` varchar(30) collate utf8_unicode_ci default NULL,
  `familiar_te` varchar(15) collate utf8_unicode_ci default NULL,
  PRIMARY KEY  (`id_alumno`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=286 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auxiliares`
--

CREATE TABLE IF NOT EXISTS `auxiliares` (
  `id_auxiliar` tinyint(4) NOT NULL auto_increment,
  `cargo` varchar(12) collate utf8_unicode_ci NOT NULL,
  `apellidos` varchar(30) collate utf8_unicode_ci NOT NULL,
  `nombres` varchar(40) collate utf8_unicode_ci NOT NULL,
  `calle` varchar(40) collate utf8_unicode_ci NOT NULL,
  `numero` varchar(6) collate utf8_unicode_ci NOT NULL,
  `localidad` varchar(30) collate utf8_unicode_ci NOT NULL,
  `telefono` varchar(16) collate utf8_unicode_ci NOT NULL,
  `dni` varchar(16) collate utf8_unicode_ci default NULL,
  `correo` varchar(64) collate utf8_unicode_ci default NULL,
  `inicio` date NOT NULL,
  PRIMARY KEY  (`id_auxiliar`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=7 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `coordinadores`
--

CREATE TABLE IF NOT EXISTS `coordinadores` (
  `id_coordinador` tinyint(4) NOT NULL auto_increment,
  `apellidos` varchar(20) collate utf8_unicode_ci NOT NULL,
  `nombres` varchar(25) collate utf8_unicode_ci NOT NULL,
  `te_contacto` varchar(15) collate utf8_unicode_ci NOT NULL,
  `celular` varchar(16) collate utf8_unicode_ci default NULL,
  `calle` varchar(30) collate utf8_unicode_ci NOT NULL,
  `numero` varchar(6) collate utf8_unicode_ci default NULL,
  `localidad` varchar(30) collate utf8_unicode_ci default NULL,
  `correo` varchar(40) collate utf8_unicode_ci default NULL,
  PRIMARY KEY  (`id_coordinador`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=32 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cursos`
--

CREATE TABLE IF NOT EXISTS `cursos` (
  `id_curso` mediumint(9) NOT NULL auto_increment,
  `num_curso` varchar(5) collate utf8_unicode_ci NOT NULL,
  `tipo` varchar(3) collate utf8_unicode_ci NOT NULL default 'FP',
  `especialidad` varchar(60) collate utf8_unicode_ci NOT NULL,
  `instructor` varchar(64) collate utf8_unicode_ci NOT NULL,
  `ciclo` varchar(4) collate utf8_unicode_ci NOT NULL default '2000',
  `fecha_inicio` date NOT NULL,
  `fecha_final` date NOT NULL,
  `horas` varchar(3) collate utf8_unicode_ci NOT NULL,
  `horario` varchar(50) collate utf8_unicode_ci NOT NULL default 'Lunes a viernes',
  `establecimiento` varchar(40) collate utf8_unicode_ci NOT NULL,
  `estado` char(1) collate utf8_unicode_ci NOT NULL default 'A',
  `motivo_baja` varchar(30) collate utf8_unicode_ci default NULL,
  `fecha_baja` date default NULL,
  PRIMARY KEY  (`id_curso`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=90 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `especialidades`
--

CREATE TABLE IF NOT EXISTS `especialidades` (
  `id_especialidad` int(11) NOT NULL auto_increment,
  `denominacion` varchar(60) collate utf8_unicode_ci NOT NULL,
  `tipo` varchar(3) collate utf8_unicode_ci NOT NULL,
  `duracion` smallint(6) NOT NULL,
  PRIMARY KEY  (`id_especialidad`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=301 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `establecimientos`
--

CREATE TABLE IF NOT EXISTS `establecimientos` (
  `id_establecimiento` tinyint(4) NOT NULL auto_increment,
  `tipo` varchar(3) collate utf8_unicode_ci NOT NULL default 'CFP',
  `numero` char(3) collate utf8_unicode_ci NOT NULL default '401',
  `nombre` varchar(40) collate utf8_unicode_ci NOT NULL,
  `calle` varchar(20) collate utf8_unicode_ci NOT NULL,
  `num_puerta` varchar(5) collate utf8_unicode_ci NOT NULL,
  `localidad` varchar(25) collate utf8_unicode_ci NOT NULL,
  `cp` varchar(8) collate utf8_unicode_ci NOT NULL,
  `telefono` varchar(15) collate utf8_unicode_ci NOT NULL,
  `correo` varchar(40) collate utf8_unicode_ci NOT NULL,
  `site` varchar(64) collate utf8_unicode_ci default 'http://',
  `distrito` varchar(20) collate utf8_unicode_ci NOT NULL default 'Vicente López',
  `coordinador` varchar(40) collate utf8_unicode_ci NOT NULL,
  PRIMARY KEY  (`id_establecimiento`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=30 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fichacurso`
--

CREATE TABLE IF NOT EXISTS `fichacurso` (
  `id_fc` tinyint(4) NOT NULL auto_increment,
  `apell_nom` varchar(70) collate utf8_unicode_ci NOT NULL,
  `nac` varchar(20) collate utf8_unicode_ci NOT NULL,
  `fecha_nac` date NOT NULL,
  `tipo_doc` varchar(10) collate utf8_unicode_ci NOT NULL,
  `num_doc` varchar(12) collate utf8_unicode_ci NOT NULL,
  `domicilio` varchar(70) collate utf8_unicode_ci NOT NULL,
  `sexo` char(1) collate utf8_unicode_ci NOT NULL default 'M',
  PRIMARY KEY  (`id_fc`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=16 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `gastos`
--

CREATE TABLE IF NOT EXISTS `gastos` (
  `id_gasto` tinyint(4) NOT NULL auto_increment,
  `fecha` date NOT NULL,
  `tipo` char(1) collate utf8_unicode_ci NOT NULL default 'g',
  `comprobante` varchar(40) collate utf8_unicode_ci default NULL,
  `responsable` varchar(60) collate utf8_unicode_ci NOT NULL,
  `debe` float default NULL,
  `haber` float default NULL,
  `destino` varchar(30) collate utf8_unicode_ci NOT NULL,
  PRIMARY KEY  (`id_gasto`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=28 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `instructores`
--

CREATE TABLE IF NOT EXISTS `instructores` (
  `id_instructor` tinyint(4) NOT NULL auto_increment,
  `apellidos` varchar(20) collate utf8_unicode_ci NOT NULL,
  `nombres` varchar(25) collate utf8_unicode_ci NOT NULL,
  `te_contacto` varchar(15) collate utf8_unicode_ci NOT NULL,
  `celular` varchar(16) collate utf8_unicode_ci default 'no tiene',
  `calle` varchar(30) collate utf8_unicode_ci NOT NULL,
  `numero` varchar(6) collate utf8_unicode_ci default NULL,
  `localidad` varchar(30) collate utf8_unicode_ci default NULL,
  `correo` varchar(40) collate utf8_unicode_ci NOT NULL,
  PRIMARY KEY  (`id_instructor`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=27 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `legajo`
--

CREATE TABLE IF NOT EXISTS `legajo` (
  `id_legajo` int(11) NOT NULL auto_increment,
  `id_alumno` int(11) NOT NULL,
  `nombre` varchar(60) collate utf8_unicode_ci NOT NULL,
  `fechanac` date NOT NULL,
  `lugarnac` varchar(50) collate utf8_unicode_ci NOT NULL,
  `estcivil` varchar(40) collate utf8_unicode_ci NOT NULL,
  `domicilio` varchar(60) collate utf8_unicode_ci NOT NULL,
  `te` varchar(20) collate utf8_unicode_ci NOT NULL,
  `plansocial` tinyint(1) NOT NULL,
  `queplan` varchar(30) collate utf8_unicode_ci NOT NULL,
  `planfamiliar` tinyint(1) NOT NULL,
  `queplanfamiliar` varchar(30) collate utf8_unicode_ci NOT NULL,
  `empleo` varchar(40) collate utf8_unicode_ci NOT NULL,
  `ubicacionempleo` varchar(40) collate utf8_unicode_ci NOT NULL,
  `educformal` varchar(50) collate utf8_unicode_ci NOT NULL,
  `abandono` tinyint(1) NOT NULL,
  `causaabandono` varchar(40) collate utf8_unicode_ci NOT NULL,
  `cursando` tinyint(1) NOT NULL,
  `cursandolugar` varchar(30) collate utf8_unicode_ci NOT NULL,
  `otroscursosfp` tinyint(1) NOT NULL,
  `otroscursosfpcuales` varchar(40) collate utf8_unicode_ci NOT NULL,
  `jefefamilia` tinyint(1) NOT NULL,
  `deportes` tinyint(1) NOT NULL,
  `deportesdonde` varchar(30) collate utf8_unicode_ci NOT NULL,
  `tiempolibre` varchar(60) collate utf8_unicode_ci NOT NULL,
  `eligioelcentro` varchar(60) collate utf8_unicode_ci NOT NULL,
  `eligioelcurso` varchar(60) collate utf8_unicode_ci NOT NULL,
  `judiciales` tinyint(1) NOT NULL,
  `causas` varchar(100) collate utf8_unicode_ci NOT NULL,
  `tratmedico` varchar(30) collate utf8_unicode_ci NOT NULL,
  `observaciones` text collate utf8_unicode_ci NOT NULL,
  PRIMARY KEY  (`id_legajo`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=33 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `miescuela`
--

CREATE TABLE IF NOT EXISTS `miescuela` (
  `id_miescuela` tinyint(4) NOT NULL auto_increment,
  `nombre` varchar(40) collate utf8_unicode_ci NOT NULL,
  `calle` varchar(30) collate utf8_unicode_ci NOT NULL,
  `numpuerta` varchar(5) collate utf8_unicode_ci NOT NULL,
  `cp` varchar(8) collate utf8_unicode_ci NOT NULL,
  `localidad` varchar(20) collate utf8_unicode_ci NOT NULL,
  `telefono` varchar(15) collate utf8_unicode_ci default NULL,
  `correo` varchar(64) collate utf8_unicode_ci default NULL,
  `site` varchar(64) collate utf8_unicode_ci default NULL,
  PRIMARY KEY  (`id_miescuela`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=5 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mov_alumnos`
--

CREATE TABLE IF NOT EXISTS `mov_alumnos` (
  `id_alumno` int(11) NOT NULL,
  `tipomov` varchar(1) collate utf8_unicode_ci NOT NULL,
  `curso` varchar(5) collate utf8_unicode_ci NOT NULL,
  `fecha` date default NULL,
  `observaciones` text collate utf8_unicode_ci,
  UNIQUE KEY `id_alumno` (`id_alumno`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `seguimiento`
--

CREATE TABLE IF NOT EXISTS `seguimiento` (
  `id_seguimiento` int(11) NOT NULL auto_increment,
  `id_alumno` varchar(4) collate utf8_unicode_ci NOT NULL,
  `rubro` varchar(20) collate utf8_unicode_ci NOT NULL,
  `empresa` varchar(30) collate utf8_unicode_ci NOT NULL,
  `estado` varchar(25) collate utf8_unicode_ci NOT NULL,
  `fecha` date NOT NULL,
  PRIMARY KEY  (`id_seguimiento`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=7 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `temporal`
--

CREATE TABLE IF NOT EXISTS `temporal` (
  `id_alumno` varchar(11) collate utf8_unicode_ci NOT NULL,
  `apellidos` varchar(30) collate utf8_unicode_ci NOT NULL,
  `nombres` varchar(30) collate utf8_unicode_ci NOT NULL,
  `sexo` char(1) collate utf8_unicode_ci NOT NULL,
  `tipo_doc` varchar(3) collate utf8_unicode_ci NOT NULL,
  `num_doc` varchar(10) collate utf8_unicode_ci NOT NULL,
  PRIMARY KEY  (`id_alumno`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
