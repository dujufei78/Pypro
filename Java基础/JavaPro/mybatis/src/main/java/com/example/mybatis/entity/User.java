package com.example.mybatis.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

/*
 * 1.使用@Data注解
 * 2.使用注解@TableName(value = "user") -----user这个是对应数据库的表名
 * 3.编写和数据库字段对应的属性
 * 4.加上文档注解@ApiModelProperty("用户的id")---里面的文字是相当于给自己看的备注
 * 5.使用@TableId(value = "id", type = IdType.AUTO) //作用是标明当前属性主键，并且type = IdType.AUTO这个代表id自增
 * */
@Data  //1
@TableName(value = "user")    //2
public class User {

    @ApiModelProperty("用户的id")  //4
    @TableId(value = "id", type = IdType.AUTO) //5
    private Integer id;  //3

    @ApiModelProperty("用户名")  //4
    private String username;  //3

    @ApiModelProperty("密码")  //4
    private String password;   //3
}

/*
 * 注解的解释
 * @Data：注解是这个来源于lombok，内置了set、get、ToString等属性类里面我们需要写的东西，就不用我们写了
 * @TableName：注解是 MyBatis-Plus 框架中的一个注解，用于标识实体类与数据库表之间的映射关系。
 * 它的作用是告诉 MyBatis-Plus 框架这个实体类对应哪个数据库表。
 * @ApiModelProperty：注解是 Swagger 框架中的一个注解，
 * 用于给实体类的属性（字段）添加额外的文档说明，以便在生成 API 文档时提供更详细的描述和信息。
 * Swagger是一个用于生成和展示 API 文档的工具，可以帮助开发人员更好地理解和使用 API。
 *
 * @TableId 注解用于标识表的主键字段，帮助 MyBatis-Plus 框架了解哪个属性在数据库中扮演主键的角色，
 * 以及如何生成主键值。这对于数据库操作和映射非常重要。
 * */