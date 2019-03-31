/*
 Navicat Premium Data Transfer

 Source Server         : 39.107.87.250_kbqa
 Source Server Type    : MySQL
 Source Server Version : 80015
 Source Host           : 39.107.87.250:3306
 Source Schema         : kbqa

 Target Server Type    : MySQL
 Target Server Version : 80015
 File Encoding         : 65001

 Date: 31/03/2019 20:13:30
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for kb_questions
-- ----------------------------
DROP TABLE IF EXISTS `kb_questions`;
CREATE TABLE `kb_questions`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `question` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '用户问题',
  `normalize_question` json COMMENT '转换的标准问题',
  `triples` json COMMENT '生成的三元组',
  `create_time` datetime(0) DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
