import { Status } from '@/api/modules/status.ts'
import { Priority } from '@/api/modules/priority.ts'

export interface Todo {
  id: number
  name: string
  detail: string
  state: Status
  priority: Priority
}
