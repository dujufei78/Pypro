package com.example.mybatis.service;

import com.baomidou.mybatisplus.extension.service.IService;
import com.example.mybatis.entity.User;


//1.继承IService这个接口，<实体类名>
public interface IUserService extends IService<User> {
}

/*
IService接口里面有mybatis-plus封装好我们经常会用到的增删改查的一些方法
里面本质上还调用了上数据层mapper，是对mapper的封装优化
*/