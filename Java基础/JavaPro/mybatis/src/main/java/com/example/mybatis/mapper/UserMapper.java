package com.example.mybatis.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.example.mybatis.entity.User;
import org.apache.ibatis.annotations.Mapper;
/*
 * 1.使用@Mapper注解 ，代表这个接口被mybatis接管
 * 2.继承BaseMapper<属性类名>
 * */
@Mapper
public interface UserMapper extends BaseMapper<User> {
}


/*
 * @Mapper：注解是 MyBatis 框架中的一个重要标识，
 * 它定义了 Mapper 接口，用于与数据库交互。使用这个注解可以简化数据库操作代码，并提供一些优势，
 * 如自动生成 SQL、类型安全性等。
 * */