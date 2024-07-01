// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:srv/GetPath.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__GET_PATH__BUILDER_HPP_
#define INTERFACES__SRV__DETAIL__GET_PATH__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces/srv/detail/get_path__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interfaces
{

namespace srv
{

namespace builder
{

class Init_GetPath_Request_path_name
{
public:
  explicit Init_GetPath_Request_path_name(::interfaces::srv::GetPath_Request & msg)
  : msg_(msg)
  {}
  ::interfaces::srv::GetPath_Request path_name(::interfaces::srv::GetPath_Request::_path_name_type arg)
  {
    msg_.path_name = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::srv::GetPath_Request msg_;
};

class Init_GetPath_Request_goal
{
public:
  explicit Init_GetPath_Request_goal(::interfaces::srv::GetPath_Request & msg)
  : msg_(msg)
  {}
  Init_GetPath_Request_path_name goal(::interfaces::srv::GetPath_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return Init_GetPath_Request_path_name(msg_);
  }

private:
  ::interfaces::srv::GetPath_Request msg_;
};

class Init_GetPath_Request_start
{
public:
  Init_GetPath_Request_start()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GetPath_Request_goal start(::interfaces::srv::GetPath_Request::_start_type arg)
  {
    msg_.start = std::move(arg);
    return Init_GetPath_Request_goal(msg_);
  }

private:
  ::interfaces::srv::GetPath_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::GetPath_Request>()
{
  return interfaces::srv::builder::Init_GetPath_Request_start();
}

}  // namespace interfaces


namespace interfaces
{

namespace srv
{

namespace builder
{

class Init_GetPath_Response_path
{
public:
  Init_GetPath_Response_path()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interfaces::srv::GetPath_Response path(::interfaces::srv::GetPath_Response::_path_type arg)
  {
    msg_.path = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::srv::GetPath_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::GetPath_Response>()
{
  return interfaces::srv::builder::Init_GetPath_Response_path();
}

}  // namespace interfaces

#endif  // INTERFACES__SRV__DETAIL__GET_PATH__BUILDER_HPP_
