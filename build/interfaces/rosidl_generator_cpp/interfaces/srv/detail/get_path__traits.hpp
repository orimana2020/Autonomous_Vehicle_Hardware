// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interfaces:srv/GetPath.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__GET_PATH__TRAITS_HPP_
#define INTERFACES__SRV__DETAIL__GET_PATH__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "interfaces/srv/detail/get_path__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'start'
// Member 'goal'
#include "geometry_msgs/msg/detail/point__traits.hpp"
// Member 'path_name'
#include "std_msgs/msg/detail/string__traits.hpp"

namespace interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const GetPath_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: start
  {
    out << "start: ";
    to_flow_style_yaml(msg.start, out);
    out << ", ";
  }

  // member: goal
  {
    out << "goal: ";
    to_flow_style_yaml(msg.goal, out);
    out << ", ";
  }

  // member: path_name
  {
    out << "path_name: ";
    to_flow_style_yaml(msg.path_name, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GetPath_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: start
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "start:\n";
    to_block_style_yaml(msg.start, out, indentation + 2);
  }

  // member: goal
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal:\n";
    to_block_style_yaml(msg.goal, out, indentation + 2);
  }

  // member: path_name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "path_name:\n";
    to_block_style_yaml(msg.path_name, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GetPath_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace interfaces

namespace rosidl_generator_traits
{

[[deprecated("use interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const interfaces::srv::GetPath_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const interfaces::srv::GetPath_Request & msg)
{
  return interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<interfaces::srv::GetPath_Request>()
{
  return "interfaces::srv::GetPath_Request";
}

template<>
inline const char * name<interfaces::srv::GetPath_Request>()
{
  return "interfaces/srv/GetPath_Request";
}

template<>
struct has_fixed_size<interfaces::srv::GetPath_Request>
  : std::integral_constant<bool, has_fixed_size<geometry_msgs::msg::Point>::value && has_fixed_size<std_msgs::msg::String>::value> {};

template<>
struct has_bounded_size<interfaces::srv::GetPath_Request>
  : std::integral_constant<bool, has_bounded_size<geometry_msgs::msg::Point>::value && has_bounded_size<std_msgs::msg::String>::value> {};

template<>
struct is_message<interfaces::srv::GetPath_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'path'
// already included above
// #include "geometry_msgs/msg/detail/point__traits.hpp"

namespace interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const GetPath_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: path
  {
    if (msg.path.size() == 0) {
      out << "path: []";
    } else {
      out << "path: [";
      size_t pending_items = msg.path.size();
      for (auto item : msg.path) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GetPath_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: path
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.path.size() == 0) {
      out << "path: []\n";
    } else {
      out << "path:\n";
      for (auto item : msg.path) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GetPath_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace interfaces

namespace rosidl_generator_traits
{

[[deprecated("use interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const interfaces::srv::GetPath_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const interfaces::srv::GetPath_Response & msg)
{
  return interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<interfaces::srv::GetPath_Response>()
{
  return "interfaces::srv::GetPath_Response";
}

template<>
inline const char * name<interfaces::srv::GetPath_Response>()
{
  return "interfaces/srv/GetPath_Response";
}

template<>
struct has_fixed_size<interfaces::srv::GetPath_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<interfaces::srv::GetPath_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<interfaces::srv::GetPath_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::srv::GetPath>()
{
  return "interfaces::srv::GetPath";
}

template<>
inline const char * name<interfaces::srv::GetPath>()
{
  return "interfaces/srv/GetPath";
}

template<>
struct has_fixed_size<interfaces::srv::GetPath>
  : std::integral_constant<
    bool,
    has_fixed_size<interfaces::srv::GetPath_Request>::value &&
    has_fixed_size<interfaces::srv::GetPath_Response>::value
  >
{
};

template<>
struct has_bounded_size<interfaces::srv::GetPath>
  : std::integral_constant<
    bool,
    has_bounded_size<interfaces::srv::GetPath_Request>::value &&
    has_bounded_size<interfaces::srv::GetPath_Response>::value
  >
{
};

template<>
struct is_service<interfaces::srv::GetPath>
  : std::true_type
{
};

template<>
struct is_service_request<interfaces::srv::GetPath_Request>
  : std::true_type
{
};

template<>
struct is_service_response<interfaces::srv::GetPath_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // INTERFACES__SRV__DETAIL__GET_PATH__TRAITS_HPP_
