# Apifox 接口同步清单

## 公共信息

| 项目 | 内容 |
| --- | --- |
| 模块 |  |
| Base Path | `/{basePath}` |
| 认证方式 | JWT 登录态 / 无需登录 / 管理端权限 |
| 返回结构 | `BaseResponse<T>` |
| 时间格式 | `yyyy-MM-dd HH:mm:ss` |
| 本次变更类型 | 新增 / 修改 / 删除 / 行为调整 |
| 兼容性 | 兼容 / 不兼容，说明原因 |

## 一、接口清单

| 序号 | 接口名称 | Method | Path | 权限 | 请求 Schemas | 响应模型 | 变更类型 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  | `GET` | `/example` | 登录用户 | `ExamplePathParams` / `ExampleQueryParams` / `ExampleHeaders` / `ExampleBody` | `BaseResponse<ExampleVo>` | 新增 |

## 二、接口详情

### 1. 接口名称

**Method**

```http
GET /example
```

**接口说明**

说明接口用途、业务规则、特殊限制。

**权限**

```text
登录用户
```

**请求参数类型**

```text
Path 参数 / Query 参数 / Body JSON / 无参数
```

**Path Params Schema**

```json
{
  "type": "object",
  "required": ["id"],
  "properties": {
    "id": {
      "type": "string",
      "description": "ID",
      "example": "123"
    }
  }
}
```

**Query Params Schema**

```json
{
  "type": "object",
  "required": [],
  "properties": {
    "pageNo": {
      "type": "integer",
      "description": "页码",
      "example": 1
    },
    "pageSize": {
      "type": "integer",
      "description": "每页条数",
      "example": 10
    }
  }
}
```

**Headers Schema**

```json
{
  "type": "object",
  "required": [],
  "properties": {
    "Authorization": {
      "type": "string",
      "description": "JWT 登录态请求头，格式为 Bearer token",
      "example": "Bearer <token>"
    }
  }
}
```

**Cookies Schema**

```json
{
  "type": "object",
  "required": [],
  "properties": {}
}
```

**Body JSON 示例**

```json
{
  "name": "示例名称"
}
```

**Body Schema**

```json
{
  "type": "object",
  "required": ["name"],
  "properties": {
    "name": {
      "type": "string",
      "description": "名称",
      "example": "示例名称"
    }
  }
}
```

**成功响应示例**

```json
{
  "code": 200,
  "msg": "操作成功",
  "data": {}
}
```

**响应模型**

```text
BaseResponse<ExampleVo>
```

**错误场景**

| code | msg | 触发条件 |
| --- | --- | --- |
|  |  |  |

**Apifox 录入提醒**

- 文档：需要新增 / 更新接口说明
- 示例：需要补充请求示例和成功响应示例
- Mock：需要配置 / 不需要
- 测试用例：需要覆盖正常场景、权限失败、参数非法、业务异常

## 三、数据模型 JSON Schema

> 所有请求模型、响应模型、分页模型、通用响应模型和枚举相关模型都必须给出 JSON Schema。请求模型包括 Path、Query、Headers、Cookies、Body。

### ExamplePathParams

```json
{
  "type": "object",
  "required": ["id"],
  "properties": {
    "id": {
      "type": "string",
      "description": "ID",
      "example": "123"
    }
  }
}
```

### ExampleQueryParams

```json
{
  "type": "object",
  "required": [],
  "properties": {
    "pageNo": {
      "type": "integer",
      "description": "页码",
      "example": 1
    },
    "pageSize": {
      "type": "integer",
      "description": "每页条数",
      "example": 10
    }
  }
}
```

### ExampleHeaders

```json
{
  "type": "object",
  "required": [],
  "properties": {
    "Authorization": {
      "type": "string",
      "description": "JWT 登录态请求头，格式为 Bearer token",
      "example": "Bearer <token>"
    }
  }
}
```

### ExampleCookies

```json
{
  "type": "object",
  "required": [],
  "properties": {}
}
```

### ExampleBody

```json
{
  "type": "object",
  "required": ["name"],
  "properties": {
    "name": {
      "type": "string",
      "description": "名称",
      "example": "示例名称"
    }
  }
}
```

### ExampleVo

```json
{
  "type": "object",
  "required": [],
  "properties": {
    "id": {
      "type": "string",
      "description": "ID",
      "example": "123"
    },
    "createdAt": {
      "type": "string",
      "format": "date-time",
      "description": "创建时间",
      "example": "2026-07-01 10:00:00"
    }
  }
}
```

## 四、枚举说明

| 字段 | 枚举值 | 含义 |
| --- | --- | --- |
| status | 1 | 启用 |
| status | 2 | 禁用 |

## 五、通用响应模型

### BaseResponseVoid

```json
{
  "type": "object",
  "required": ["code", "msg", "data"],
  "properties": {
    "code": {
      "type": "integer",
      "description": "响应码",
      "example": 200
    },
    "msg": {
      "type": "string",
      "description": "响应消息",
      "example": "操作成功"
    },
    "data": {
      "type": "null",
      "description": "空数据"
    }
  }
}
```

### BaseResponseExampleVo

```json
{
  "type": "object",
  "required": ["code", "msg", "data"],
  "properties": {
    "code": {
      "type": "integer",
      "description": "响应码",
      "example": 200
    },
    "msg": {
      "type": "string",
      "description": "响应消息",
      "example": "操作成功"
    },
    "data": {
      "$ref": "#/components/schemas/ExampleVo"
    }
  }
}
```

## 六、本次 Apifox 同步结论

- 是否涉及 API 变更：是 / 否
- 需要新增接口：
- 需要修改接口：
- 需要删除接口：
- 需要新增 / 修改数据模型：
- 需要同步权限说明：是 / 否
- 需要同步错误码：是 / 否
- 需要补充 Mock：是 / 否
- 需要补充测试用例：是 / 否
