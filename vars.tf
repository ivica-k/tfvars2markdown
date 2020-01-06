variable "some_var_1" {
  type = string
  default = "foo"
  description = "Some description var_1"
}

variable "some_var_2" {
  type = bool
  default = false
  description = "Some description var_2"
}

variable "some_var_3" {
  type = number
  default = "12"
  description = "Some description var_3"
}

variable "some_var_4" {
  type = list(string)
  default = ["foo", "bar", "baz"]
}

variable "some_var_5" {
  type = list(bool)
  default = [true, true, false]
  description = "Some description var_5. This is a very long description with unicode characters ćšđž"
}

variable "some_var_6" {
  type = list(number)
  default = [1, 2, 3]
  description = "Some description var_6"
}

variable "some_var_7" {
  type = any
  description = "Some description var_7. No defaults provided"
}

variable "some_var_8" {
  description = "Some description var_8. No type or default provided"
}

variable "some_var_9" {
  description = "Some description var_8. No type or default provided"
}

resource "null_resource" "opa_null" {}

